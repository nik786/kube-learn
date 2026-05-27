import os
import re
import json
import time
import boto3
import shutil

from datetime import datetime, timedelta
from botocore.config import Config

from utils import (
    make_request,
    get_grafana_url
)

# =========================================================
# CONFIG
# =========================================================

BASE_PATH = os.getenv("BASE_PATH", "/app")

S3_BUCKET = os.getenv("S3_BUCKET_NAME")

RETENTION_DAYS = int(
    os.getenv("RETENTION_DAYS", 5)
)

boto_config = Config(
    retries={
        "max_attempts": 5,
        "mode": "standard"
    },
    connect_timeout=10,
    read_timeout=60
)

s3_client = boto3.client(
    "s3",
    config=boto_config
)

# =========================================================
# HELPERS
# =========================================================
def safe_name(name):

    return re.sub(
        r"[^a-zA-Z0-9_-]+",
        "_",
        name
    )


def get_date_folder():

    return datetime.now().strftime(
        "%d-%m-%Y"
    )


def get_timestamp():

    return datetime.now().strftime(
        "%d-%m-%Y_%H-%M-%S"
    )


# =========================================================
# PATHS
# =========================================================
def get_paths(env):

    date = get_date_folder()

    relative_path = os.path.join(
        env,
        date,
        "datasources"
    )

    # =====================================================
    # LOCAL PVC PATH
    # =====================================================
    local_backup = os.path.join(
        BASE_PATH,
        "backup",
        relative_path
    )

    # =====================================================
    # S3 PATH
    # =====================================================
    s3_base = relative_path.replace(
        os.sep,
        "/"
    )

    os.makedirs(
        local_backup,
        exist_ok=True
    )

    return s3_base, local_backup


# =========================================================
# CLEANUP
# Deletes old backup folders from PVC
# =========================================================
def cleanup_old_backups(env):

    backup_root = os.path.join(
        BASE_PATH,
        "backup",
        env
    )

    if not os.path.exists(backup_root):
        return

    now = datetime.now()

    for folder in os.listdir(backup_root):

        folder_path = os.path.join(
            backup_root,
            folder
        )

        if not os.path.isdir(folder_path):
            continue

        try:

            folder_date = datetime.strptime(
                folder,
                "%d-%m-%Y"
            )

        except Exception:
            continue

        age = now - folder_date

        if age > timedelta(days=RETENTION_DAYS):

            print(f"🗑️ Removing old backup: {folder_path}")

            shutil.rmtree(
                folder_path,
                ignore_errors=True
            )


# =========================================================
# S3 UPLOAD
# =========================================================
def s3_put_with_retry(
    bucket,
    key,
    body,
    retries=3
):

    for attempt in range(retries):

        try:

            s3_client.put_object(
                Bucket=bucket,
                Key=key,
                Body=body
            )

            print(f"☁️ Uploaded to S3: {key}")

            return True

        except Exception as e:

            print(
                f"⚠️ Upload failed "
                f"(attempt {attempt+1}): {e}"
            )

            time.sleep(2 ** attempt)

    return False


# =========================================================
# SAVE + UPLOAD
# =========================================================
def save_and_upload(
    data,
    datasource_uid,
    local_base,
    s3_base
):

    safe_uid = safe_name(
        datasource_uid
    )

    timestamp = get_timestamp()

    file_name = (
        f"{safe_uid}_{timestamp}.json"
    )

    local_path = os.path.join(
        local_base,
        file_name
    )

    # =====================================================
    # SAVE LOCALLY (PVC)
    # =====================================================
    with open(local_path, "w") as f:

        json.dump(
            data,
            f,
            indent=2
        )

    print(f"✅ Saved locally: {local_path}")

    # =====================================================
    # S3 UPLOAD
    # =====================================================
    s3_key = f"{s3_base}/{file_name}"

    with open(local_path, "rb") as f:

        s3_put_with_retry(
            S3_BUCKET,
            s3_key,
            f
        )


# =========================================================
# BACKUP DATASOURCES
# =========================================================
def backup_datasources(
    env,
    names=None
):

    # =====================================================
    # CLEANUP OLD PVC FILES
    # =====================================================
    cleanup_old_backups(env)

    # =====================================================
    # PATHS
    # =====================================================
    s3_base, local_backup = get_paths(env)

    grafana_url = get_grafana_url(env)

    print("\n====================================")
    print("🚀 DATASOURCE BACKUP STARTED")
    print("====================================")

    print(f"ENV: {env}")
    print(f"FILTER: {names}")
    print(f"S3 PATH: {s3_base}")
    print(f"LOCAL PATH: {local_backup}")

    # =====================================================
    # FETCH ALL DATASOURCES
    # =====================================================
    response = make_request(
        env,
        f"{grafana_url}/api/datasources"
    )

    if not response or response.status_code != 200:

        print("❌ Failed to fetch datasources")

        return

    datasources = response.json()

    if not datasources:

        print("⚠️ No datasources found")

        return

    processed = 0

    # =====================================================
    # LOOP DATASOURCES
    # =====================================================
    for datasource in datasources:

        uid = datasource.get("uid")

        name = datasource.get(
            "name",
            "unknown"
        )

        # =================================================
        # FILTER
        # =================================================
        if names != "all" and names:

            if uid not in names:
                continue

        # =================================================
        # FETCH FULL DATASOURCE JSON
        # =================================================
        datasource_response = make_request(
            env,
            f"{grafana_url}/api/datasources/uid/{uid}"
        )

        if (
            not datasource_response
            or datasource_response.status_code != 200
        ):

            print(
                f"❌ Failed datasource: {uid}"
            )

            continue

        print(
            f"➡️ Backing up datasource: "
            f"{name}"
        )

        save_and_upload(
            datasource_response.json(),
            uid,
            local_backup,
            s3_base
        )

        processed += 1

        time.sleep(0.2)

    # =====================================================
    # SUMMARY
    # =====================================================
    print("\n====================================")

    if processed == 0:

        print(
            "⚠️ No datasources matched filter"
        )

    else:

        print(
            f"🎉 Total datasources backed up: "
            f"{processed}"
        )

    print("====================================\n")

