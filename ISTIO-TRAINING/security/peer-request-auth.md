## 🔐 Istio Authentication Overview

### 📘 PeerAuthentication (Service-to-Service)

| **Concept**         | **Details**                                                                 |
|---------------------|------------------------------------------------------------------------------|
| **Purpose**         | Verifies the identity of the client (service) making the connection          |
| **Mechanism**       | Uses **Mutual TLS (mTLS)**                                                   |
| **Default Mode**    | **Permissive** – Accepts both plain text and mTLS connections                |
| **STRICT Mode**     | Enforces **only mTLS** connections                                           |
| **Resource Used**   | `PeerAuthentication`                                                         |
| **Scope**           | Can be applied mesh-wide, per namespace, or per workload                    |
| **Graceful Rollout**| Permissive mode allows gradual adoption of mTLS across the mesh              |

---

### 🔐 RequestAuthentication (End-User Authentication)

| **Concept**         | **Details**                                                                 |
|---------------------|------------------------------------------------------------------------------|
| **Purpose**         | Authenticates the **end-user** of the service                                |
| **Mechanism**       | Validates **JWT tokens** attached to the requests                            |
| **Resource Used**   | `RequestAuthentication`                                                      |
| **Supported Providers** | OpenID Connect providers: **Auth0**, **Firebase**, **Google Auth**, **Keycloak**, **ORY Hydra** |
| **Use Case**        | Validate requests from users, mobile apps, or browsers                       |
| **How it Works**    | JWT token is validated against issuer and audience                          |

---

### 🔄 Summary of Authentication Types

| **Authentication Type** | **Resource**             | **Use Case**                       | **Mechanism**              |
|--------------------------|--------------------------|------------------------------------|----------------------------|
| Service-to-Service       | `PeerAuthentication`     | Secure communication between services | Mutual TLS (mTLS)          |
| End-User                 | `RequestAuthentication`  | Verify user identity in requests    | JWT Token Validation       |

> ✅ PeerAuthentication secures service-to-service traffic.  
> ✅ RequestAuthentication secures user-facing traffic.


