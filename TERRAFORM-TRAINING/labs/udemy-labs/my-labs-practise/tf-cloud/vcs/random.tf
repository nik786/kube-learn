

resource "random_string" "random" {
    length = 16
}

resource "random_pet" "server" {
    length = 2
}

module "s3" {
    source = "terraform-aws-modules/s3-bucket/aws//examples/complete"
    version = "2.10.0"
}

