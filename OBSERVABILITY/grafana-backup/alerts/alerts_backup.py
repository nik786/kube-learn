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
            s3_client.put_object(Bucket=bucket, Key=key, Body=body)
            print(f"☁️ Uploaded: {key}")
            return True
        except Exception as e:
            print(f"⚠️ Upload failed ({attempt+1}): {e}")
            time.sleep(2 ** attempt)
    return False


def s3_get_with_retry(bucket, key, retries=3):
    for attempt in range(retries):
        try:
            return s3_client.get_object(Bucket=bucket, Key=key)
        except Exception as e:
            print(f"⚠️ Download failed ({attempt+1}): {e}")
            time.sleep(2 ** attempt)
    return None


def s3_list_with_retry(bucket, prefix, retries=3):
    for attempt in range(retries):
        try:
            return s3_client.list_objects_v2(Bucket=bucket, Prefix=prefix)
        except Exception as e:
            print(f"⚠️ List failed ({attempt+1}): {e}")
            time.sleep(2 ** attempt)
    return {}


# -------- HELPERS --------
def safe_name(name):
    return re.sub(r'[^a-zA-Z0-9_-]+', '_', name.strip())


def get_date_folder():
    return datetime.now().strftime("%d-%m-%Y")


def resolve_type(alert_type):
    return "syst/all" if alert_type == "all" else "syst"


def get_paths(env, alert_type):
    folder = resolve_type(alert_type)

    s3_base = f"backup/alerts/{folder}"

    base = r"C:\grafana"

    if folder == "syst":
        local_backup = os.path.join(base, "backup", "alerts", env)
        local_restore = os.path.join(base, "restore", "alerts", env)
    else:
        local_backup = os.path.join(base, "backup", "alerts", env, "all")
        local_restore = os.path.join(base, "restore", "alerts", env, "all")

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
            folder_date = datetime.strptime(folder, "%d-%m-%Y")
        except:
            continue

        if now - folder_date > timedelta(days=days):
            shutil.rmtree(path, ignore_errors=True)
            print(f"🗑️ Deleted: {path}")


# -------- SAVE --------
def save_and_upload(data, name, local_base, s3_base):
    date = get_date_folder()

    safe = safe_name(name)

    local_folder = os.path.join(local_base, date)
    os.makedirs(local_folder, exist_ok=True)

    file_name = f"{safe}_{date}.json"
    local_path = os.path.join(local_folder, file_name)

    with open(local_path, "w") as f:
        json.dump(data, f, indent=2)

    print(f"✅ Saved locally: {local_path}")

    s3_key = f"{s3_base}/{date}/{file_name}"

    with open(local_path, "rb") as f:
        s3_put_with_retry(S3_BUCKET, s3_key, f)


# -------- BACKUP (UNIFIED) --------
def backup_alerts(env, names=None, alert_type="syst"):
    s3_base, local_backup, _ = get_paths(env, alert_type)
    grafana_url = get_grafana_url(env)

    cleanup_old_local_backups(local_backup)

    print(f"\n🚀 Backup alerts | ENV={env} | TYPE={alert_type} | NAMES={names}")

    res = make_request(env, f"{grafana_url}/api/v1/provisioning/alert-rules")

    if not res or res.status_code != 200:
        print("❌ Failed to fetch alerts")
        return

    alerts = res.json()
    processed = 0

    for alert in alerts:
        title = alert.get("title", "unknown")

        if names and title not in names:
            continue

        print(f"➡️ Backing up: {title}")

        save_and_upload(alert, title, local_backup, s3_base)

        processed += 1
        time.sleep(0.2)

    if processed == 0:
        print("⚠️ No alerts matched")
    else:
        print(f"\n🎉 Total alerts backed up: {processed}")


# -------- OPTIONAL WRAPPER --------
def backup_all_alerts(env, alert_type="syst"):
    return backup_alerts(env, None, alert_type)


# -------- RESTORE (LOCAL ONLY) --------
def restore_alerts_from_s3(env, date, files=None, alert_type="syst"):
    s3_base, _, local_restore = get_paths(env, alert_type)

    prefix = f"{s3_base}/{date}/"

    print(f"🔍 Fetching from S3: {prefix}")

    cleanup_old_local_backups(local_restore)

    res = s3_list_with_retry(S3_BUCKET, prefix)

    if "Contents" not in res:
        print("❌ No backups found")
        return

    local_folder = os.path.join(local_restore, date)
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

        print(f"\n📥 Downloading: {file_name}")

        response = s3_get_with_retry(S3_BUCKET, key)

        if not response:
            continue

        data = response["Body"].read()

        local_path = os.path.join(local_folder, file_name)

        with open(local_path, "wb") as f:
            f.write(data)

        print(f"✅ Saved to: {local_path}")
        downloaded += 1

    print(f"\n🎉 Total alerts downloaded: {downloaded}")


####



def restore_alerts_to_grafana(env, date, files=None, alert_type="syst"):
    _, _, local_restore = get_paths(env, alert_type)

    local_folder = os.path.join(local_restore, date)

    if not os.path.exists(local_folder):
        print("❌ Local restore folder not found. Run restore_alerts_from_s3 first.")
        return

    grafana_url = get_grafana_url(env)

    file_set = set(files) if files else None
    restored = 0

    for file_name in os.listdir(local_folder):

        if file_set and file_name not in file_set:
            continue

        file_path = os.path.join(local_folder, file_name)

        print(f"🚀 Restoring alert: {file_name}")

        with open(file_path, "r") as f:
            data = json.load(f)

        res = make_request(
            env,
            f"{grafana_url}/api/v1/provisioning/alert-rules",
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

    print(f"\n🎉 Total alerts restored: {restored}")
