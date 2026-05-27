import os
import re
import json
import time
import boto3
import shutil

from datetime import datetime, timedelta

from botocore.config import Config

from utils import make_request, get_grafana_url


# =========================================================
# CONFIG
# =========================================================
S3_BUCKET = "grafana-backup-01"

boto_config = Config(
    retries={"max_attempts": 5, "mode": "standard"},
    connect_timeout=10,
    read_timeout=60
)

s3_client = boto3.client(
    "s3",
    config=boto_config
)


# =========================================================
# RETRY WRAPPERS
# =========================================================
def s3_put_with_retry(bucket, key, body, retries=3):

    for attempt in range(retries):

        try:

            s3_client.put_object(
                Bucket=bucket,
                Key=key,
                Body=body
            )

            print(f"☁️ Uploaded: {key}")

            return True

        except Exception as e:

            print(f"⚠️ Upload failed ({attempt+1}): {e}")

            time.sleep(2 ** attempt)

    return False


def s3_get_with_retry(bucket, key, retries=3):

    for attempt in range(retries):

        try:

            return s3_client.get_object(
                Bucket=bucket,
                Key=key
            )

        except Exception as e:

            print(f"⚠️ Download failed ({attempt+1}): {e}")

            time.sleep(2 ** attempt)

    return None


def s3_list_with_retry(bucket, prefix, retries=3):

    for attempt in range(retries):

        try:

            return s3_client.list_objects_v2(
                Bucket=bucket,
                Prefix=prefix
            )

        except Exception as e:

            print(f"⚠️ List failed ({attempt+1}): {e}")

            time.sleep(2 ** attempt)

    return {}


# =========================================================
# HELPERS
# =========================================================
def safe_name(name):

    return re.sub(
        r'[^a-zA-Z0-9_-]+',
        '_',
        name.strip()
    )


def get_date_folder():

    return datetime.now().strftime("%d-%m-%Y")


def get_timestamp():

    return datetime.now().strftime("%d-%m-%Y_%H-%M-%S")


def get_paths():

    base = "/home/nik/Desktop/git_ops/script/py/grafana"

    date = get_date_folder()

    relative_path = os.path.join(
        "contact-points",
        date
    )

    # -----------------------------------------------------
    # LOCAL
    # -----------------------------------------------------
    local_backup = os.path.join(
        base,
        "backup",
        relative_path
    )

    local_restore = os.path.join(
        base,
        "restore",
        relative_path
    )

    # -----------------------------------------------------
    # S3
    # -----------------------------------------------------
    s3_base = relative_path.replace(os.sep, "/")

    os.makedirs(local_backup, exist_ok=True)

    os.makedirs(local_restore, exist_ok=True)

    return s3_base, local_backup, local_restore


def clean_contact_point(cp):

    cp.pop("uid", None)
    cp.pop("id", None)
    cp.pop("orgId", None)
    cp.pop("created", None)
    cp.pop("updated", None)
    cp.pop("permissions", None)
    cp.pop("accessControl", None)

    return cp


# =========================================================
# CLEANUP
# =========================================================
def cleanup_old_local_backups(base_path, days=5):

    if not os.path.exists(base_path):
        return

    now = datetime.now()

    for folder in os.listdir(base_path):

        path = os.path.join(base_path, folder)

        try:

            folder_date = datetime.strptime(
                folder,
                "%d-%m-%Y"
            )

        except:
            continue

        if now - folder_date > timedelta(days=days):

            shutil.rmtree(
                path,
                ignore_errors=True
            )

            print(f"🗑️ Deleted: {path}")


# =========================================================
# SAVE
# =========================================================
def save_and_upload(data, name, local_base, s3_base):

    safe = safe_name(name)

    timestamp = get_timestamp()

    file_name = f"{safe}_{timestamp}.json"

    local_path = os.path.join(
        local_base,
        file_name
    )

    with open(local_path, "w") as f:

        json.dump(
            data,
            f,
            indent=2
        )

    print(f"✅ Saved: {local_path}")

    # -----------------------------------------------------
    # S3 KEY
    # -----------------------------------------------------
    s3_key = f"{s3_base}/{file_name}"

    with open(local_path, "rb") as f:

        s3_put_with_retry(
            S3_BUCKET,
            s3_key,
            f
        )


# =========================================================
# BACKUP
# =========================================================
# =========================================================
# BACKUP
# =========================================================
def backup_contact_points(env, names=None):

    s3_base, local_backup, _ = get_paths()

    grafana_url = get_grafana_url(env)

    cleanup_old_local_backups(local_backup)

    print(
        f"\n🚀 Backup started | "
        f"ENV={env} | "
        f"NAMES={names}"
    )

    # -----------------------------------------------------
    # FETCH CONTACT POINTS
    # -----------------------------------------------------
    res = make_request(
        env,
        f"{grafana_url}/api/v1/provisioning/contact-points"
    )

    if not res or res.status_code != 200:

        print("❌ Failed to fetch contact points")

        return

    cps = res.json()

    if not cps:

        print("⚠️ No contact points found")

        return

    processed = 0

    for cp in cps:

        name = cp.get("name", "unknown")

        # -------------------------------------------------
        # FILTER BY NAMES
        # -------------------------------------------------
        if names:

            # normalize current contact point name
            name_clean = name.strip().lower()

            # normalize input names
            normalized_names = [
                n.strip().lower()
                for n in names
            ]

            if name_clean not in normalized_names:
                continue

        print(f"➡️ Backing up: {name}")

        clean_cp = clean_contact_point(cp)

        save_and_upload(
            clean_cp,
            name,
            local_backup,
            s3_base
        )

        processed += 1

        time.sleep(0.2)

    # -----------------------------------------------------
    # FINAL SUMMARY
    # -----------------------------------------------------
    if processed == 0:

        print("⚠️ No contact points matched your criteria")

    else:

        print(
            f"\n🎉 Total contact points backed up: "
            f"{processed}"
        )


# =========================================================
# RESTORE FROM S3
# =========================================================
def restore_contact_points_from_s3(env, date, files=None):

    s3_base, _, local_restore = get_paths()

    cleanup_old_local_backups(local_restore)

    prefix = f"{s3_base}/{date}/"

    print(f"🔍 Fetching from S3: {prefix}")

    res = s3_list_with_retry(
        S3_BUCKET,
        prefix
    )

    if "Contents" not in res:

        print("❌ No backups found")

        return

    local_folder = os.path.join(
        local_restore,
        date
    )

    os.makedirs(local_folder, exist_ok=True)

    file_set = set(files) if files else None

    downloaded = 0

    for obj in res["Contents"]:

        key = obj["Key"]

        if key.endswith("/"):
            continue

        file_name = key.split("/")[-1]

        if file_set and file_name not in file_set:
            continue

        print(f"📥 Downloading: {file_name}")

        response = s3_get_with_retry(
            S3_BUCKET,
            key
        )

        if not response:
            continue

        data = response["Body"].read()

        local_path = os.path.join(
            local_folder,
            file_name
        )

        with open(local_path, "wb") as f:

            f.write(data)

        print(f"✅ Saved locally: {local_path}")

        downloaded += 1

    print(f"\n🎉 Total downloaded: {downloaded}")


# =========================================================
# RESTORE TO GRAFANA
# =========================================================
def restore_contact_points_to_grafana(
    env,
    date,
    files=None
):

    _, _, local_restore = get_paths()

    local_folder = os.path.join(
        local_restore,
        date
    )

    if not os.path.exists(local_folder):

        print(
            "❌ Run restore_contact_points_from_s3 first"
        )

        return

    grafana_url = get_grafana_url(env)

    file_set = set(files) if files else None

    restored = 0

    for file_name in os.listdir(local_folder):

        if file_set and file_name not in file_set:
            continue

        file_path = os.path.join(
            local_folder,
            file_name
        )

        print(f"🚀 Restoring: {file_name}")

        with open(file_path, "r") as f:

            cp = json.load(f)

        cp = clean_contact_point(cp)

        res = make_request(
            env,
            f"{grafana_url}/api/v1/provisioning/contact-points",
            method="POST",
            json=cp
        )

        if res and res.status_code in [200, 202]:

            print(f"✅ Restored: {cp.get('name')}")

            restored += 1

        else:

            print(f"❌ Failed: {file_name}")

            if res:
                print(res.status_code, res.text)

    print(f"\n🎉 Total restored: {restored}")

