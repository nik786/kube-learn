I want to make execution in following way

python run.py --action backup_dashboards  --env syst --upload_dashboard_ids all
python run.py --action backup_dashboards --env syst  --upload_dashboard_ids adhwkmz,adhwkmz


python run.py --action backup_contact_points --env syst --upload_contact_point_names "dsml-shared-email" 
python run.py --action backup_contact_points --env syst --upload_contact_point_names all


python run.py --action backup_alerts --env syst  --upload_alert_names test01,test02
python run.py --action backup_alerts  --env syst --upload_alert_names all

python run.py --action backup_datasources --env syst --upload_datasource_ids all
python run.py --action backup_datasources --env syst --upload_datasource_ids aflu1w1m1v474f,dfidfideey134f


curl -X GET "http://127.0.0.1:3007/api/dashboards/uid/rYdddlPWk"   -H "Authorization: Bearer "

curl -X GET "http://127.0.0.1:3007/api/datasources/uid/dfidfideey134f" \
  -H "Authorization: Bearer " \
  -H "Content-Type: application/json"


curl "http://127.0.0.1:3007/api/v1/alerts?alert_group_id=I68T24C13IFW1" \
  --request GET \
  --header "Authorization: Bearer " \
  --header "Content-Type: application/json" 



curl -X GET "http://127.0.0.1:3007/api/dashboards/uid/rYdddlPWk"   -H "Authorization: Bearer"

curl -X GET "http://127.0.0.1:3007/api/search?type=dash-db"   -H "Authorization: Bearer"



export SYST_GRAFANA_API_KEY=""

python run.py --action restore_contact_points_from_s3 --env syst --date 28-04-2026
python run.py --action restore_contact_points_from_s3 --env syst --date 28-04-2026 --files 0d-ms_dsml-shared-email_28-04-2026.json

python run.py --action restore_contact_points_to_grafana --env syst --date 28-04-2026 --files 0d-ms_dsml-shared-email_28-04-2026.json


python run.py --action restore_dashboards_from_s3 --env syst --date 28-04-2026 --path syst --files Node_Exporter_Full_28-04-2026.json,Kubernetes_Cluster_Prometheus__28-04-2026.json
python run.py --action restore_dashboards_from_s3 --env syst --date 28-04-2026
python run.py --action restore_dashboards_to_grafana --env syst --date 28-04-2026 --path syst --files test01_28-04-2026.json,test02_28-04-2026.json

python run.py --action restore_alerts_from_s3 --env syst --date 28-04-2026 --path syst --files test01_28-04-2026.json,test02_28-04-2026.json
python run.py --action restore_alerts_from_s3 --env syst --date 28-04-2026
python run.py --action restore_alerts_to_grafana --env syst --date 28-04-2026 --path syst --files test01_28-04-2026.json,test02_28-04-2026.json


python grafana.py --action restore_dashboard --key syst/single/08-04-2026/file.json
python grafana.py --action restore_alert --key syst/alerts/08-04-2026/file.json
python grafana.py --action restore_contact --key syst/contact_points/08-04-2026/file.json


kind create cluster

kubectl cluster-info
kubectl get nodes

kind create cluster --name dev-cluster























