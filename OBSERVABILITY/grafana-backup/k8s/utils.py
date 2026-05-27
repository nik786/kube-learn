import os
import requests


# =========================================================
# GRAFANA URLS
# =========================================================
PROD_GRAFANA_URL = os.getenv("PROD_GRAFANA_URL")
TEST_GRAFANA_URL = os.getenv("TEST_GRAFANA_URL")
SYST_GRAFANA_URL = os.getenv("SYST_GRAFANA_URL")


# =========================================================
# API KEYS
# =========================================================
PROD_API_KEY = os.getenv("PROD_GRAFANA_API_KEY")
TEST_API_KEY = os.getenv("TEST_GRAFANA_API_KEY")
SYST_API_KEY = os.getenv("SYST_GRAFANA_API_KEY")


# =========================================================
# ENV -> URL
# =========================================================
def get_grafana_url(env):

    env_map = {
        "prod": PROD_GRAFANA_URL,
        "test": TEST_GRAFANA_URL,
        "syst": SYST_GRAFANA_URL
    }

    url = env_map.get(env)

    if not url:
        raise ValueError(f"❌ Missing Grafana URL for env: {env}")

    return url


# =========================================================
# ENV -> API KEY
# =========================================================
def get_api_key(env):

    key_map = {
        "prod": PROD_API_KEY,
        "test": TEST_API_KEY,
        "syst": SYST_API_KEY
    }

    api_key = key_map.get(env)

    if not api_key:
        raise ValueError(f"❌ Missing API key for env: {env}")

    return api_key


# =========================================================
# HEADERS
# =========================================================
def get_headers(env):

    api_key = get_api_key(env)

    return {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }


# =========================================================
# GENERIC REQUEST
# =========================================================
def make_request(
    env,
    url,
    method="GET",
    json=None,
    timeout=30
):

    try:

        headers = get_headers(env)

        response = requests.request(
            method=method,
            url=url,
            headers=headers,
            json=json,
            timeout=timeout
        )

        return response

    except requests.exceptions.RequestException as e:

        print(f"❌ Request failed: {e}")

        return None

