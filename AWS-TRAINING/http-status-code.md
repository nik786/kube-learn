

# HTTP Status Codes Explained

| Code | Meaning               | Difference                                                                                   |
|------|-----------------------|---------------------------------------------------------------------------------------------|
| 200  | OK                    | Request succeeded, and the server responded with the requested data.                         |
| 201  | Created               | Request succeeded, and the server created a new resource.                                    |
| 301  | Moved Permanently     | The requested resource has been permanently moved to a new URL.                              |
| 302  | Found                 | The requested resource is temporarily located at a different URL.                           |
| 303  | See Other             | The response to the request can be found under a different URI using a GET method.           |
| 304  | Not Modified          | The resource has not been modified since the last request, so the cached version can be used.|
| 305  | Use Proxy             | The requested resource must be accessed through a proxy.                                     |
| 400  | Bad Request           | The server could not understand the request due to invalid syntax.                           |
| 401  | Unauthorized          | Authentication is required and has failed or has not yet been provided.                     |
| 403  | Forbidden             | The server understands the request, but the client does not have permission to access the resource. |
| 404  | Not Found             | The server cannot find the requested resource.                                               |
| 500  | Internal Server Error | The server encountered an error and could not complete the request.                          |
| 501  | Not Implemented       | The server does not support the functionality required to fulfill the request.               |
| 503  | Service Unavailable   | The server is temporarily unable to handle the request due to maintenance or overload.       |
