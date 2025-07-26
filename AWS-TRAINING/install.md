


- [ecs-agent](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-agent-install.html)

```

curl -O https://s3.us-west-2.amazonaws.com/amazon-ecs-agent-us-west-2/amazon-ecs-init-latest.amd64.deb
dpkg -i amazon-ecs-init-latest.amd64.deb


curl -O https://s3.us-west-2.amazonaws.com/amazon-ecs-agent-us-west-2/amazon-ecs-init-latest.x86_64.rpm
yum localinstall -y amazon-ecs-init-latest.x86_64.rpm

systemctl start ecs


```

- [kubectl](https://docs.aws.amazon.com/eks/latest/userguide/install-kubectl.html)

```

curl -O https://s3.us-west-2.amazonaws.com/amazon-eks/1.33.0/2025-05-01/bin/linux/amd64/kubectl

aws sts get-caller-identity

aws eks update-kubeconfig --region region-code --name my-cluster



```

- [eksctl](https://eksctl.io/installation/)

```


ARCH=amd64
PLATFORM=$(uname -s)_$ARCH

curl -sLO "https://github.com/eksctl-io/eksctl/releases/latest/download/eksctl_$PLATFORM.tar.gz"


curl -sL "https://github.com/eksctl-io/eksctl/releases/latest/download/eksctl_checksums.txt" | grep $PLATFORM | sha256sum --check

tar -xzf eksctl_$PLATFORM.tar.gz -C /tmp && rm eksctl_$PLATFORM.tar.gz

sudo install -m 0755 /tmp/eksctl /usr/local/bin && rm /tmp/eksctl

```

```
yum install amazon-cloudwatch-agent

https://amazoncloudwatch-agent.s3.amazonaws.com/amazon_linux/arm64/latest/amazon-cloudwatch-agent.rpm

https://amazoncloudwatch-agent.s3.amazonaws.com/amazon_linux/amd64/latest/amazon-cloudwatch-agent.rpm

sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl -a fetch-config -m ec2 -s -c file:configuration-file-path

systemctl start amazon-cloudwatch-agent

```


https://docs.aws.amazon.com/systems-manager/latest/userguide/agent-install-al2.html

```
yum install -y https://s3.amazonaws.com/ec2-downloads-windows/SSMAgent/latest/linux_amd64/amazon-ssm-agent.rpm

yum install -y https://s3.amazonaws.com/ec2-downloads-windows/SSMAgent/latest/linux_arm64/amazon-ssm-agent.rpm

systemctl status amazon-ssm-agent

systemctl start amazon-ssm-agent

```

awscli

```

https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html

yum remove awscli

curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install

curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install --bin-dir /usr/local/bin --install-dir /usr/local/aws-cli --update


curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"


```


```

curl -O https://get.helm.sh/helm-v3.16.2-linux-amd64.tar.gz

tar xvf helm-v3.16.2-linux-amd64.tar.gz Copy. ...
mv linux-amd64/helm /usr/local/bin Copy. ...
rm helm-v3.16.2-linux-amd64.tar.gz Copy


```
https://releases.hashicorp.com/terraform

wget https://releases.hashicorp.com/terraform/1.12.2/terraform_1.12.2_linux_amd64.zip

```
yum install openssl11-devel
yum install gcc openssl-devel bzip2-devel libffi-devel zlib-devel -y
dnf install python3.11
python3.11 -m pip --version
python3.11 -m pip --version
amazon-linux-extras install python3
yum install python3 python3-pip -y
python3 -m venv ansible_env
source ansible_env/bin/activate
pip3 install ansible==2.19

```

amazon-linux-extras install docker
service docker start
usermod -a -G docker ec2-user
docker ps



yum install iperf telnet nc 















