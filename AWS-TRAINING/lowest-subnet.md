

## 📊 AWS Subnet Size Limitations

| CIDR Block | Total IPs | Usable IPs in AWS | Allowed in AWS? | Notes |
|------------|-----------|-------------------|------------------|-------|
| `/32`      | 1         | 0                 | ❌ No             | Single IP, used for host routes only |
| `/31`      | 2         | 0                 | ❌ No             | Special case for point-to-point links (RFC 3021) |
| `/30`      | 4         | 0                 | ❌ No             | All IPs consumed by AWS reserved + network/broadcast |
| `/29`      | 8         | 3                 | ❌ No             | Not enough usable IPs after AWS reserves 5 |
| `/28`      | 16        | 11                | ✅ Yes            | **Smallest subnet size allowed** in most AWS services |
