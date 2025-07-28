


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
        "arn:aws:s3:::vp-ep-test-01",
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

accesspoint


```

{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::359994326874:user/user01"
      },
      "Action": [
          "s3:GetObject",
          "s3:PutObject"
          
          ],
      "Resource": [
        "arn:aws:s3:us-east-1:364657694739:accesspoint/user01-ap/object/dataset1/*"
        
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

```
aws s3api list-objects-v2 \
  --bucket arn:aws:s3:us-east-1:364657694739:accesspoint/user01-ap \
  --prefix dataset1/


aws s3api get-object \
  --bucket arn:aws:s3:us-east-1:364657694739:accesspoint/user01-ap \
  --key dataset1/sample.txt \
  output.txt


aws s3api put-object \
  --bucket arn:aws:s3:us-east-1:364657694739:accesspoint/user01-ap \
  --key dataset1/newfile.txt \
  --body ./newfile.txt


aws sts get-caller-identity

```

https://www.youtube.com/watch?v=Mqo4rt12IL0
