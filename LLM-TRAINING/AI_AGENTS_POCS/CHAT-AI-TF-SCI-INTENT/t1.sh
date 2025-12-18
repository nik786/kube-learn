JENKINS_URLS=("http://127.0.0.1:8080" "http://localhost:8080/job/test_01")

for JENKINS_URL in "${JENKINS_URLS[@]}"; do
    echo "$JENKINS_URL" >> out.txt
done

# Check the content of out.txt
cat out.txt
