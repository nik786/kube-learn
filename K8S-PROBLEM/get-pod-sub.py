import subprocess
import json
import argparse

def get_matching_pods(api_urls, namespaces, keywords, cert_path, key_path, cacert_path):
    matching_pods = []

    for namespace in namespaces:
        for url in api_urls:
            for keyword in keywords:
                command = [
                    "curl", "-ks", "--cert", cert_path, "--key", key_path, "--cacert", cacert_path,
                    f"{url}/api/v1/namespaces/{namespace}/pods",
                    "|",
                    "jq", "-c",
                    f".items[] | select(.status.phase == \"Running\" and (.spec.containers[].image | contains(\"{keyword}\"))) | {{name: .metadata.name, status: .status.phase, image: .spec.containers[].image}}"
                ]
                process = subprocess.Popen(" ".join(command), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                stdout, stderr = process.communicate()

                if process.returncode == 0:
                    try:
                        pods_data = stdout.strip().split("\n")
                        matching_pods.extend(pods_data)
                    except Exception as e:
                        print(f"Error parsing output: {e}")
                else:
                    print(f"Error executing command: {stderr}")

    return matching_pods

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fetch data from Kubernetes API URLs")
    parser.add_argument("-k", "--keywords", nargs='+', required=True, help="Keywords to search for in container images")
    args = parser.parse_args()

    cert_path = "/etc/kubernetes/pki/users/k8s-admin/k8s-admin.crt"
    key_path = "/etc/kubernetes/pki/users/k8s-admin/k8s-admin.key"
    cacert_path = "/etc/kubernetes/pki/ca.crt"

    # Define the Kubernetes API URLs
    api_urls = ["https://192.168.56.70:6443"]

    # Define the namespaces to search for pods
    namespaces = ["default", "kube-system"]

    # Call the function to get matching pods
    matching_pods = get_matching_pods(api_urls, namespaces, args.keywords, cert_path, key_path, cacert_path)

    # Print the information about matching running pods
    for pod in matching_pods:
        print(pod)
