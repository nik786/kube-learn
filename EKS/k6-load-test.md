
```

import http from 'k6/http';
import { check, sleep } from 'k6';

export const options = {
  stages: [
    { duration: '30s', target: 10 }, // Ramp up to 10 VUs (virtual users)
    { duration: '1m', target: 10 },  // Stay at 10 VUs
    { duration: '10s', target: 0 },  // Ramp down to 0 VUs
  ],
};

export default function () {
  const res = http.get('https://test-api.k6.io/public/crocodiles/');

  check(res, {
    'status is 200': (r) => r.status === 200,
    'body is not empty': (r) => r.body.length > 0,
  });

  sleep(1); // Wait 1 second between requests
}

k6 run loadtest.js


You’ll get a live summary with metrics like:

Requests per second

Avg, Min, Max response times

HTTP failure rate

VU activity


```
