java -javaagent:opentelemetry-javaagent.jar \
-Dotel.service.name=hello-service \
-Dotel.traces.exporter=none \
-Dotel.metrics.exporter=none \
-Dotel.logs.exporter=otlp \
-Dotel.instrumentation.logback-appender.enabled=true \
-Dotel.exporter.otlp.endpoint=http://localhost:4318 \
-Dotel.exporter.otlp.protocol=http/protobuf \
-jar target/hello-0.0.1.jar
