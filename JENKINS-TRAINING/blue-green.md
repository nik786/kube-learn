

# Blue-Green Deployment Pipeline for AWS EKS using Jenkins, Helm, and kubectl

| **Step** | **Stage** | **Tool** | **Action** | **Command / Description** |
|----------|-----------|----------|------------|----------------------------|
| 1 | Git Strategy | Git | Use separate `main` (prod) and `develop` branches | Merge to `main` triggers prod deployment via Jenkins webhook |
| 2 | Jenkins Parameters | Jenkins | Accept runtime params | Use `app_name`, `app_version`, and `docker_image` as input parameters in pipeline |
| 3 | Identify Active Color | kubectl | Check current live color | `kubectl get svc ${APP_NAME}-svc -o jsonpath='{.spec.selector.color}'` |
| 4 | Determine Target Color | Jenkins logic | Set opposite color | If active is `blue`, deploy `green`, else deploy `blue` |
| 5 | Render Helm Chart | Helm | Prepare new version | `helm upgrade --install ${APP_NAME}-${COLOR} ./helm/${APP_NAME} -f ./helm/${APP_NAME}/values-${COLOR}.yaml --set image.tag=${APP_VERSION} --set image.repository=${DOCKER_IMAGE} --namespace ${APP_NAME}` |
| 6 | Wait for Rollout | kubectl | Ensure pods are ready | `kubectl rollout status deployment/${APP_NAME}-${COLOR} -n ${APP_NAME}` |
| 7 | Run Smoke Tests | kubectl | Optional health check | `kubectl run smoke-test --rm -i --tty --image=busybox --restart=Never -- wget ${APP_NAME}-${COLOR}.${APP_NAME}.svc.cluster.local:8080/health` |
| 8 | Switch Traffic | kubectl | Update service selector | `kubectl patch svc ${APP_NAME}-svc -n ${APP_NAME} -p '{"spec": {"selector": {"app": "'${APP_NAME}'", "color": "'${COLOR}'"}}}'` |
| 9 | Validate Switch | kubectl | Confirm service pointing | `kubectl get svc ${APP_NAME}-svc -o jsonpath='{.spec.selector}' -n ${APP_NAME}` |
| 10 | Cleanup Old Color (Optional) | Helm | Remove old release | `helm uninstall ${APP_NAME}-${OLD_COLOR} -n ${APP_NAME}` |
| 11 | Notify Team | Jenkins | Send result | Notify via Slack/email on success/failure with current active color |

## Best Practices
- 🟢 Always run health checks before switching traffic
- 🔄 Keep old version live for rollback
- 🗂️ Use separate Helm value files: `values-blue.yaml`, `values-green.yaml`
- 🔐 Use RBAC, secrets encryption, and audit logs on your EKS cluster
- 📦 Helm chart values should be parameterized (image, replicas, resources, etc.)

## Jenkins Parameters
- `app_name` = your app (e.g. `myapp`)
- `app_version` = version tag (e.g. `1.3.2`)
- `docker_image` = image repo (e.g. `123456789.dkr.ecr.us-east-1.amazonaws.com/myapp`)

## Branching Strategy
- `main` = production (protected branch)
- `develop` = staging/testing
- Create `release/*` branches for major releases



