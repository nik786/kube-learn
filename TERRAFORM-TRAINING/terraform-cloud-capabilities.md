

What is Sentinel Policy?
-------------------------

Sentinel is the Policy-as-Code product from HashiCorp that automatically enforces logic-based policy
decisions across all HashiCorp Enterprise products. It allows users to implement policy-as-code in a
similar way to how Terraform implements infrastructure-as-code. If enabled, Sentinel is run between
the terraform plan and apply stages of the workflow.


• EC2 instances must have a Name tag.
• EC2 instances must be of type t2.micro, t2.small, or t2.medium.


https://github.com/btkrausen/hashicorp

order they appear in this file. We are also making use of sentinel modules to include some functions
used by our Sentinel policies


```

sentinel.hcl
-------------

module "tfplan-functions" {
    source = "https://raw.githubusercontent.com/hashicorp/terraform-guides/
              master/governance/third-generation/common-functions/tfplan-functions/
              tfplan-functions.sentinel"
}

module "tfconfig-functions" {
          source = "https://raw.githubusercontent.com/hashicorp/terraform-guides
                  /master/governance/third-generation/common-functions/tfconfigfunctions/tfconfig-functions.sentinel"
}
policy "enforce-mandatory-tags" {
          enforcement_level = "advisory"
}
policy "restrict-ec2-instance-type" {
          enforcement_level = "hard-mandatory"
}

```

| Enforcement Level  | Description  |
|-------------------|--------------|
| **Advisory**  | The policy is allowed to fail. However, a warning should be shown to the user or logged. |
| **Soft Mandatory**  | The policy must pass unless an override is specified. The semantics of "override" are specific to each Sentinel-enabled application. This level provides privilege separation and ensures non-repudiation, as an explicit override is required. |
| **Hard Mandatory**  | The policy must pass no matter what. The only way to override a hard mandatory policy is to explicitly remove it. This is the default enforcement level and should be used when an override is not possible. |


```

Now let’s update our code to specify an instance size that is not allowed via policy.
Navigate to the web_server resource block and
update the instance_type to m5.large




resource "aws_instance" "web_server" {
      ami = data.aws_ami.ubuntu.id
      instance_type = "m5.large"
      subnet_id = aws_subnet.public_subnets["public_subnet_1
"].id
      security_groups = [aws_security_group.vpc-ping.id,
      aws_security_group.ingress-ssh.id, aws_security_group.vpc-web.id]
      associate_public_ip_address = true
      key_name = aws_key_pair.generated.key_name

      connection {
            user = "ubuntu"
            private_key = tls_private_key.generated.private_key_pem
            host = self.public_ip
}


```
















