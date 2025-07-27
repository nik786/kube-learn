


user1

```

{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "VisualEditor0",
      "Effect": "Allow",
      "Action": [
        "s3:GetAccessPoint",
        "s3:ListAllMyBuckets",
        "s3:ListAccessPoints",
        "s3:ListMultiRegionAccessPoints",
        "s3:ListBucket"
      ],
      "Resource": "*"
    }
  ]
}
```


s3-bucket

```

{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "AWS": "*"
      },
      "Action": "*",
      "Resource": [
        "arn:aws:s3:::vp-ep-test-01/*"
      ],
      "Condition": {
        "StringEquals": {
          "s3:DataAccessPointAccount": "359994326874"
        }
      }
    }
  ]
}

```
