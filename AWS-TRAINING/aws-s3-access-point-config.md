


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
            "Sid": "AllowUser01AccessToDataset1Only",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::359994326874:user/user01"
            },
            "Action": [
                "s3:GetObject",
                "s3:PutObject"
            ],
            "Resource": "arn:aws:s3:us-east-1:359994326874:accesspoint/user01-ap/object/dataset1/*"
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

aws s3 ls s3://arn:aws:s3:us-east-1:841860927337:accesspoint/user01-ap/dataset1/


accesspoint/user01-ap/object/dataset1/

aws sts get-caller-identity

```

https://www.youtube.com/watch?v=Mqo4rt12IL0

S3 Access Points

S3 Gateway Endpoint for S3 Access

Use PrivateLink Endpoint

Egress-Only Gateway


- [how-we-cut-40-in-nat-gateway-costs](https://medium.com/zesty-engineering/how-we-cut-40-in-nat-gateway-costs-640a9b3f9a48)

- [reduce-cost-and-improve-security-with-amazon-vpc-endpoints](https://www.kubeblogs.com/reduce-cost-and-improve-security-with-amazon-vpc-endpoints/)  
  
- [deployment-of-node-js-app-on-aws](https://medium.com/@survasepradips147/deployment-of-node-js-app-on-aws-ecs-fargate-with-terraform-and-github-actions-d67b121bd780)

- [dynamodb-expert](https://towardsaws.com/become-an-amazon-dynamodb-expert-9674a87d4ece)
- [building-a-scalable-batch-processing-serverless-pipeline-with-aws-step-functions](https://medium.com/@hobballah.yasser/building-a-scalable-batch-processing-serverless-pipeline-with-aws-step-functions-and-batch-fe13146e1e17)
- [split-cost-allocation-data-for-amazon-eks](https://medium.com/@hirsch.elad/split-cost-allocation-data-for-amazon-eks-deb59dbd344a)
- [serverless-best-practices-with-powertools](https://blog.localstack.cloud/serverless-best-practices-with-powertools/)
- [aws-terraform-2024-ecs-cluster](https://medium.com/@mrprmode/aws-terraform-2024-ecs-cluster-on-autoscaling-ec2-with-rds-8806a8147153)
- [real-time-data-pipeline-with-apache-kafka](https://medium.com/@traviszack22/real-time-data-pipeline-with-apache-kafka-2f827397cb54)
- [step-by-step-guide-to-building-an-aws-sns-application](https://medium.com/@traviszack22/step-by-step-guide-to-building-an-aws-sns-application-2bb2673d1f94)
- [reduce-cost-and-improve-security-with-amazon-vpc-endpoints](https://www.kubeblogs.com/reduce-cost-and-improve-security-with-amazon-vpc-endpoints/)
