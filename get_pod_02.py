import requests
import argparse
requests.packages.urllib3.disable_warnings()

def get_matching_pods(api_urls, namespaces, keywords, cert_paths, cacert):
    """
    Fetches information about pods matching specified keywords from the Kubernetes API.

    Args:
    - api_urls (list): List of URLs of the Kubernetes API.
    - namespaces (list): List of namespaces to search for pods.
    - keywords (list): List of keywords to search for in container images.
    - cert_paths (list): List containing paths to the client certificate and key files.
    - cacert (str): Path to the CA certificate file.

    Returns:
    - list: A list of dictionaries containing pod information (name, status, image).
    """
    matching_pods = []

    for namespace in namespaces:
        for url in api_urls:
            for keyword in keywords:
                api_url = f"{url}/api/v1/namespaces/{namespace}/pods"
                try:
                    # Send the request with the CA certificate
                    response = requests.get(api_url, cert=cert_paths, verify=cacert)

                    # Check if the request was successful
                    if response.status_code == 200:
                        data = response.json()
                        for pod in data.get("items", []):
                            for container in pod["spec"].get("containers", []):
                                if any(keyword in container["image"] for keyword in keywords):
                                    name = pod.get("metadata", {}).get("name", "N/A")
                                    status = pod.get("status", {}).get("phase", "N/A")
                                    image = ", ".join(container["image"] for container in pod["spec"]["containers"] if any(keyword in container["image"] for keyword in keywords))
                                    if status == "Running":  # Check if the pod is running
                                        matching_pods.append({"name": name, "status": status, "image": image})
                    elif response.status_code != 404:  # Check if status code is not 404
                        print(f"Failed to fetch data from {api_url}. Status code: {response.status_code}")
                except requests.exceptions.RequestException as e:
                    print(f"Error occurred while connecting to {api_url}: {e}")

    return matching_pods

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fetch data from Kubernetes API URLs")
    parser.add_argument("-k", "--keywords", nargs='+', required=True, help="Keywords to search for in container images")
    args = parser.parse_args()

    # Define the Kubernetes API URLs
    api_urls = ["https://192.168.56.70:6443"]

    # Define the namespaces to search for pods
    namespaces = ["default", "kube-system"]

    # Define the certificate paths as a list
    cert_paths = ["/etc/kubernetes/pki/users/k8s-admin/k8s-admin.crt", "/etc/kubernetes/pki/users/k8s-admin/k8s-admin.key"]
    cacert = "/etc/kubernetes/pki/ca.crt"  # Path to the CA certificate file

    # Call the function to get matching pods
    matching_pods = get_matching_pods(api_urls, namespaces, args.keywords, cert_paths, cacert)

    # Print the information about matching running pods
    for pod in matching_pods:
        print(f"Pod Name: {pod['name']},\nStatus: {pod['status']},\nImage: {pod['image']}")

