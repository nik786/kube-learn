

# Blue-Green Deployment Pipeline for AWS EKS using Jenkins, Helm, and kubectl

| **Step** | **Stage** | **Tool**   | **Action** | **Command / Description** |
|----------|-----------|------------|------------|----------------------------|
| 1 | Git Strategy | Git | Use `main` for production | Merge to `main` triggers deployment via Jenkins webhook |
| 2 | Jenkins Parameters | Jenkins | Accept runtime parameters | `app_name`, `app_version`, `docker_image` as input to pipeline |
| 3 | Identify Active Selector | kubectl | Check current live deployment label | `kubectl get svc ${APP_NAME}-svc -o jsonpath='{.spec.selector.label}'` |
| 4 | Determine Target Selector | Jenkins logic | Select the non-live label (e.g., blue or green) | If active is `blue`, target is `green`, and vice versa |
| 5 | Deploy with Helm | Helm | Deploy to target label using Helm | `helm upgrade --install ${APP_NAME}-${TARGET_LABEL} ./helm/${APP_NAME} -f ./helm/${APP_NAME}/values-${TARGET_LABEL}.yaml --set image.tag=${APP_VERSION} --set image.repository=${DOCKER_IMAGE} --namespace ${APP_NAME}` |
| 6 | Wait for Rollout | kubectl | Ensure target pods are running | `kubectl rollout status deployment/${APP_NAME}-${TARGET_LABEL} -n ${APP_NAME}` |
| 7 | Smoke Test | kubectl | Optional health check before traffic switch | `kubectl run smoke-test --rm -i --tty --image=busybox --restart=Never -- wget ${APP_NAME}-${TARGET_LABEL}.${APP_NAME}.svc.cluster.local:8080/health` |
| 8 | Switch Live Traffic | kubectl | Patch service selector to new label | `kubectl patch svc ${APP_NAME}-svc -n ${APP_NAME} -p '{"spec": {"selector": {"app": "'${APP_NAME}'", "label": "'${TARGET_LABEL}'"}}}'` |
| 9 | Validate Service | kubectl | Confirm service is pointing correctly | `kubectl get svc ${APP_NAME}-svc -o jsonpath='{.spec.selector}' -n ${APP_NAME}` |
| 10 | Cleanup Old Deployment (Optional) | Helm | Uninstall non-active deployment | `helm uninstall ${APP_NAME}-${OLD_LABEL} -n ${APP_NAME}` |
| 11 | Notification | Jenkins | Send deployment status | Use Slack/email to notify team with result and active label |

---

## Best Practices

- ✅ Use dedicated Helm values files: `values-blue.yaml`, `values-green.yaml`
- 🔄 Keep non-live deployment running until new one is stable
- 🛡️ Secure cluster with proper RBAC and secrets management
- 🚀 Enable `readinessProbes` and `livenessProbes` for smooth rollout
- 📄 Use Helm templating for image, tag, replica count, and labels

---

## Jenkins Parameters

| Parameter      | Description |
|----------------|-------------|
| `app_name`     | Name of the application (e.g., `myapp`) |
| `app_version`  | Version/tag of Docker image (e.g., `1.3.2`) |
| `docker_image` | Full ECR image path (e.g., `123456789.dkr.ecr.us-east-1.amazonaws.com/myapp`) |

---

## Branching Strategy

- `main`: Production branch (protected)
- `develop`: Dev/staging testing
- `release/*`: Optional release branches for QA




