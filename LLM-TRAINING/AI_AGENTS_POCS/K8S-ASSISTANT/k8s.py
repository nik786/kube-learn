import requests

API_URL = "http://127.0.0.1:8001/api/v1/namespaces/default/pods"

def main():
    resp = requests.get(API_URL)
    resp.raise_for_status()

    data = resp.json()
    pods = data.get("items", [])

    for pod in pods:
        name = pod["metadata"]["name"]
        state = pod["status"]["phase"].lower()

        print(f"name: {name}")
        print(f"state: {state}")
        print("count: 1")
        print("-" * 20)

if __name__ == "__main__":
    main()

