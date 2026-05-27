import os
import re
import json
import time
import boto3
import shutil
from datetime import datetime, timedelta
from botocore.config import Config
from utils import make_request, get_grafana_url

# -------- CONFIG --------
S3_BUCKET = "grafana-backup-01"

boto_config = Config(
    retries={"max_attempts": 5, "mode": "standard"},
    connect_timeout=10,
    read_timeout=60
)

s3_client = boto3.client("s3", config=boto_config)

# -------- RETRY WRAPPERS --------
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


# -------- HELPERS --------
def safe_name(name):
    return re.sub(r'[^a-zA-Z0-9_-]+', '_', name)


def get_date_folder():
    return datetime.now().strftime("%d-%m-%Y-%M-%H")


def get_paths(env, ds_type):

    date = get_date_folder()

    base = r"/home/nik/Desktop/git_ops/script/py/grafana"

    # STRUCTURE
    # syst/12-05-2026-56-16/datasources/

    relative_path = os.path.join(
        env,
        date,
        "datasources"
    )

    # LOCAL
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

    # S3
    s3_base = relative_path.replace(os.sep, "/")

    os.makedirs(local_backup, exist_ok=True)
    os.makedirs(local_restore, exist_ok=True)

    return s3_base, local_backup, local_restore



# -------- CLEANUP --------
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


# -------- SAVE --------
def save_and_upload(data, datasource_uid, local_base, s3_base):

    safe = safe_name(datasource_uid)

    local_folder = local_base

    os.makedirs(local_folder, exist_ok=True)

    # aflu1w1m1v474f.json
    file_name = f"{safe}.json"

    local_path = os.path.join(
        local_folder,
        file_name
    )

    with open(local_path, "w") as f:
        json.dump(data, f, indent=2)

    print(f"✅ Saved: {local_path}")

    s3_key = f"{s3_base}/{file_name}"

    with open(local_path, "rb") as f:

        s3_put_with_retry(
            S3_BUCKET,
            s3_key,
            f
        )


# -------- BACKUP DATASOURCES --------
def backup_datasources(env, names=None, path="syst"):

    s3_base, local_backup, _ = get_paths(
        env,
        path
    )

    grafana_url = get_grafana_url(env)

    cleanup_old_local_backups(local_backup)

    print(
        f"\n🚀 Datasource backup started "
        f"| ENV={env} "
        f"| PATH={path} "
        f"| IDS={names}"
    )

    # -------- FETCH ALL DATASOURCES --------
    res = make_request(
        env,
        f"{grafana_url}/api/datasources"
    )

    if not res or res.status_code != 200:
        print("❌ Failed to fetch datasources")
        return

    datasources = res.json()

    if not datasources:
        print("⚠️ No datasources found")
        return

    processed = 0

    for ds in datasources:

        uid = ds.get("uid")
        name = ds.get("name", "unknown")

        # FILTER IDS
        if names:
            if uid not in names:
                continue

        # FETCH FULL DATASOURCE
        d = make_request(
            env,
            f"{grafana_url}/api/datasources/uid/{uid}"
        )

        if not d or d.status_code != 200:

            print(f"❌ Failed to fetch datasource: {uid}")
            continue

        print(f"➡️ Backing up datasource: {name}")

        save_and_upload(
            d.json(),
            uid,
            local_backup,
            s3_base
        )

        processed += 1

        time.sleep(0.2)

    # FINAL SUMMARY
    if processed == 0:
        print("⚠️ No datasources matched your criteria")

    else:
        print(
            f"\n🎉 Total datasources backed up: "
            f"{processed}"
        )


# -------- RESTORE FROM S3 --------
def restore_datasources_from_s3(
    env,
    date,
    files,
    db_type
):

    s3_base, _, local_restore = get_paths(
        env,
        db_type
    )

    prefix = f"{env}/{date}/datasources"

    if db_type == "all":
        prefix = f"{prefix}/all"

    print(f"🔍 Fetching datasources from S3: {prefix}")

    cleanup_old_local_backups(local_restore)

    res = s3_list_with_retry(
        S3_BUCKET,
        prefix
    )

    if "Contents" not in res:
        print("❌ No datasource backups found")
        return

    local_folder = local_restore

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
            print(f"❌ Failed to download: {file_name}")
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

    if downloaded == 0:
        print("⚠️ No matching datasource files found")

    else:
        print(
            f"\n🎉 Total datasources downloaded: "
            f"{downloaded}"
        )


# -------- RESTORE TO GRAFANA --------
def restore_datasources_to_grafana(
    env,
    date,
    files,
    db_type
):

    _, _, local_restore = get_paths(
        env,
        db_type
    )

    local_folder = local_restore

    if not os.path.exists(local_folder):

        print(
            "❌ Local restore folder not found. "
            "Run restore from S3 first."
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
            data = json.load(f)

        res = make_request(
            env,
            f"{grafana_url}/api/datasources",
            method="POST",
            json=data
        )

        if res and res.status_code in [200, 202]:

            print(f"✅ Restored: {file_name}")

            restored += 1

        else:

            print(f"❌ Failed: {file_name}")

            if res:
                print(res.status_code, res.text)

    print(f"\n🎉 Total restored: {restored}")
