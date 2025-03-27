import requests
import argparse
requests.packages.urllib3.disable_warnings()


def get_nginx_pods(api_urls, namespaces, pod_name, cert, cacert):
    """
    Fetches information about pods running nginx image from the Kubernetes API.

    Args:
    - api_urls (list): List of URLs of the Kubernetes API.
    - namespaces (list): List of namespaces to search for pods.
    - pod_name (str): Name of the pod to search for.
    - cert (tuple): Tuple containing paths to the client certificate and key files.
    - cacert (str): Path to the CA certificate file.

    Returns:
    - list: A list of dictionaries containing pod information (name, status, image).
    """
    nginx_pods = []

    for namespace in namespaces:
        for url in api_urls:
            api_url = f"{url}/api/v1/namespaces/{namespace}/pods/{pod_name}"
            try:
                # Send the request
                response = requests.get(api_url, cert=cert, verify=False)

                # Check if the request was successful
                if response.status_code == 200:
                    data = response.json()
                    # Check if the pod contains an nginx container
                    if any("nginx" in container["image"] for container in data["spec"]["containers"]):
                        name = data.get("metadata", {}).get("name", "N/A")
                        status = data.get("status", {}).get("phase", "N/A")
                        image = ", ".join(container["image"] for container in data["spec"]["containers"] if "nginx" in container["image"])
                        nginx_pods.append({"name": name, "status": status, "image": image})
                elif response.status_code != 404:  # Check if status code is not 404
                    print(f"Failed to fetch data from {api_url}. Status code: {response.status_code}")
            except requests.exceptions.RequestException as e:
                print(f"Error occurred while connecting to {api_url}: {e}")

    return nginx_pods

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fetch data from Kubernetes API URLs")
    parser.add_argument("-p", "--pod-name", required=True, help="Name of the pod to search for")
    args = parser.parse_args()

    # Define the Kubernetes API URLs
    api_urls = ["https://192.168.56.70:6443"]

    # Define the namespaces to search for pods
    namespaces = ["default", "kube-system"]

    # Define the certificate paths
    cert = ("/etc/kubernetes/pki/users/k8s-admin/k8s-admin.crt", "/etc/kubernetes/pki/users/k8s-admin/k8s-admin.key")
    cacert = "/etc/kubernetes/pki/users/k8s-admin/k8s-admin.crt"

    # Call the function to get nginx pods
    nginx_pods = get_nginx_pods(api_urls, namespaces, args.pod_name, cert, cacert)

    # Print the information about nginx pods
    for pod in nginx_pods:
        print(f"Pod Name: {pod['name']}, Status: {pod['status']}, Image: {pod['image']}")
