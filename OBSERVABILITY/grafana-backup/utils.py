import os
import requests

# -------- GRAFANA URLS --------
PROD_GRAFANA_URL = "http://127.0.0.1:3007"
TEST_GRAFANA_URL = "http://127.0.0.1:3007"
SYST_GRAFANA_URL = "http://127.0.0.1:3007"

# -------- API KEYS --------
PROD_API_KEY = os.getenv("PROD_GRAFANA_API_KEY")
TEST_API_KEY = os.getenv("TEST_GRAFANA_API_KEY")
SYST_API_KEY = os.getenv("SYST_GRAFANA_API_KEY")


# -------- ENV → URL --------
def get_grafana_url(env):
    if env == "prod":
        return PROD_GRAFANA_URL
    elif env == "test":
        return TEST_GRAFANA_URL
    elif env == "syst":
        return SYST_GRAFANA_URL
    else:
        raise ValueError(f"Invalid env: {env}")


# -------- ENV → API KEY --------
def get_api_key(env):
    if env == "prod":
        return PROD_API_KEY
    elif env == "test":
        return TEST_API_KEY
    elif env == "syst":
        return SYST_API_KEY
    else:
        raise ValueError(f"Invalid env: {env}")


# -------- HEADERS --------
def get_headers(env):
    api_key = get_api_key(env)

    if not api_key:
        raise ValueError(f"❌ Missing API key for env: {env}")

    return {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }


# -------- GENERIC REQUEST --------
def make_request(env, url, method="GET", json=None):
    try:
        headers = get_headers(env)

        if method == "GET":
            return requests.get(url, headers=headers, timeout=10)

        elif method == "POST":
            return requests.post(url, headers=headers, json=json, timeout=10)

        elif method == "PUT":
            return requests.put(url, headers=headers, json=json, timeout=10)

        elif method == "DELETE":
            return requests.delete(url, headers=headers, timeout=10)

    except Exception as e:
        print(f"❌ Request failed: {e}")
        return None
