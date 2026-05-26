while true; do
  curl -X POST http://localhost:4318/v1/logs \
  -H "Content-Type: application/json" \
  -d "{
    \"resourceLogs\": [{
      \"resource\": {
        \"attributes\": [{
          \"key\": \"service.name\",
          \"value\": {\"stringValue\": \"demo-service\"}
        }]
      },
      \"scopeLogs\": [{
        \"logRecords\": [{
          \"timeUnixNano\": \"$(date +%s%N)\",
          \"severityNumber\": 9,
          \"severityText\": \"INFO\",
          \"body\": {
            \"stringValue\": \"Log generated at $(date)\"
          }
        }]
      }]
    }]
  }"
  sleep 2
done

