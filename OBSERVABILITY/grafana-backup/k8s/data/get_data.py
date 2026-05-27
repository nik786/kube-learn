import os
import json
import time
import boto3
from datetime import datetime
from botocore.config import Config

from utils import (
    get_grafana_url,
    make_request
)

# -------- CONFIG --------
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

# -------- DATE --------
def get_date_folder():

    return datetime.now().strftime("%d-%m-%Y-%H-%M")


# -------- RETRY WRAPPER --------
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

            print(f"⚠️ Upload failed ({attempt + 1}): {e}")

            time.sleep(2 ** attempt)

    return False


# -------- GET DATA --------
def get_data(env):

    grafana_url = get_grafana_url(env)

    url = f"{grafana_url}/api/dashboards/uid/rYdddlPWk"

    response = make_request(
        env,
        url
    )

    if not response:

        print("❌ No response received")

        return

    if response.status_code != 200:

        print(f"❌ Failed: {response.status_code}")
        print(response.text)

        return

    data = response.json()

    # -------- PRINT OUTPUT --------
    print(json.dumps(data, indent=2))

    # -------- DATE FOLDER --------
    # Example:
    # 14-05-2026-17-45

    date_folder = get_date_folder()

    # -------- LOCAL STRUCTURE --------
    # /backup/syst/14-05-2026-17-45/data.json

    local_folder = os.path.join(
        "/home/nik/Desktop/git_ops/script/py/grafana/backup",
        env,
        date_folder
    )

    os.makedirs(local_folder, exist_ok=True)

    local_file = os.path.join(
        local_folder,
        "data.json"
    )

    # -------- WRITE LOCAL FILE --------
    with open(local_file, "w") as f:

        json.dump(
            data,
            f,
            indent=2
        )

    print(f"✅ Local file saved: {local_file}")

    # -------- S3 STRUCTURE --------
    # syst/14-05-2026-17-45/data.json

    s3_key = f"{env}/{date_folder}/data.json"

    # -------- UPLOAD TO S3 --------
    with open(local_file, "rb") as f:

        s3_put_with_retry(
            S3_BUCKET,
            s3_key,
            f
        )

    print(f"☁️ Uploaded to S3: {s3_key}")
