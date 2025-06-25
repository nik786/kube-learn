

```

terraform show -json terraform.tfstate | jq '
  .values.root_module.child_modules[]
  | select(.address == "module.web_sg")
  | .resources[]
  | select(.address == "module.web_sg.aws_security_group.this")
  | {
      arn: .values.arn,
      egress_cidr_blocks: [.values.egress[].cidr_blocks[]]
    }'



terraform state show module.web_sg.aws_security_group.this




```
