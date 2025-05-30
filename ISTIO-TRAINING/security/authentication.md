
## Authentication in Istio

- Authentication verifies identity before allowing access
- In Istio, this means: Can service X access Service Y?
- Key components:
    - Principal: The requesting service
    - Action: The request type(GET,POST)
    - Object: The target service
