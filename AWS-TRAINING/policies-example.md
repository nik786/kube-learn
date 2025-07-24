

# AWS Policy Examples

## 1. Identity-based Policy
**Attached to:** IAM users, groups, or roles  
**Purpose:** Grants permissions to an identity

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "s3:GetObject",
        "s3:ListBucket"
      ],
      "Resource": [
        "arn:aws:s3:::my-bucket",
        "arn:aws:s3:::my-bucket/*"
      ]
    }
  ]
}

```



Allows a user to list and read objects from my-bucket

## Resource-based Policy

Attached to: AWS resources (like S3 buckets, Lambda functions)
Purpose: Grants permissions to a principal on the resource

```

{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowAccountBAccess",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::222222222222:root"
      },
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::my-bucket/*"
    }
  ]
}

```


Allows users from AWS Account B to access objects in my-bucket

## Service Control Policy (SCP)

Attached to: AWS Organizations account or organizational unit (OU)
Purpose: Sets permission boundaries across accounts

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "DenyEC2",
      "Effect": "Deny",
      "Action": "ec2:*",
      "Resource": "*"
    }
  ]
}

```

Denies all EC2 actions in an account, even if IAM permissions allow it.

# IAM Policy Types – JSON Structure Differences

| Type                     | Attached To                    | Who It Grants Access To                   | JSON Key Differences                                                             | Example Use Case                               |
|--------------------------|--------------------------------|--------------------------------------------|----------------------------------------------------------------------------------|------------------------------------------------|
| **Identity-based Policy**| IAM Users, Groups, Roles       | The **identity** itself                    | `"Effect"`, `"Action"`, `"Resource"`                                           | Grant user access to read S3 buckets           |
| **Resource-based Policy**| AWS Resources (e.g., S3 Bucket)| A **principal** (IAM user, role, service)  | Includes `"Principal"` to define **who** can access the resource                | Allow another AWS account to access an S3 file |
| **Service Control Policy (SCP)**| AWS Organization or OU         | Applies to all identities in target account| No `"Principal"` or `"Resource"`; uses `"Action"` + `"Effect"` + `"Condition"` | Deny use of EC2 in specific accounts           |

## 🔍 Key Differences in JSON Body

| Feature          | Identity-based             | Resource-based              | SCP                                      |
|------------------|-----------------------------|------------------------------|-------------------------------------------|
| `"Principal"`     | ❌ Not used                 | ✅ Required                   | ❌ Not used                                |
| `"Resource"`      | ✅ Required                 | ✅ Required                   | ❌ Not used (affects **all** resources)    |
| `"Effect"`        | ✅ Allow or Deny           | ✅ Allow or Deny             | ✅ Only **Deny** or **Allow** (org-wide)   |
| Attach Location   | IAM (user/group/role)      | Directly to AWS resource     | AWS Organization / OU / Account           |
| Scope             | Specific identities         | Specific resources           | Broad – affects entire AWS accounts       |

> 📝 **Note**:  
- **SCPs** don't grant permissions by themselves — they set permission boundaries.
- **Resource-based** policies are the only ones that include the `"Principal"` element explicitly.
- **Identity-based** policies grant permissions to the identities they're attached to.









