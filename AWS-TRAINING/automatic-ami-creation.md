
EC2 instance must be SSM-managed (SSM Agent installed & IAM role with SSM permissions).

IAM Role with AmazonEC2FullAccess and AmazonSSMFullAccess

Step-by-Step:
Create an SSM Automation Document or use AWS prebuilt:

Name: AWS-CreateImage

Run Automation via Console or CLI:





```
aws ssm start-automation-execution \
  --document-name "AWS-CreateImage" \
  --parameters \
    InstanceId=i-0abcd1234efgh5678,NoReboot=true
```

```
  aws ec2 create-image \
  --instance-id i-0abcd1234efgh5678 \
  --name "MyAppImage-$(date +%Y%m%d-%H%M%S)" \
  --no-reboot
```


```

  {
  "builders": [{
    "type": "amazon-ebs",
    "region": "ap-south-1",
    "source_ami": "ami-12345678", // base AMI used by your current instance
    "instance_type": "t3.medium",
    "ssh_username": "ubuntu",
    "ami_name": "custom-ami-{{timestamp}}"
  }],
  "provisioners": [
    {
      "type": "file",
      "source": "packages.list",
      "destination": "/tmp/packages.list"
    },
    {
      "type": "shell",
      "script": "install_packages.sh"
    }
  ]
}

```

packer build ami-builder.json



apt install -y inotify-tools awscli packer

watch_and_trigger_packer.sh

```

#!/bin/bash

LOG_FILE="/var/log/dpkg.log"
INOTIFY_CMD=$(which inotifywait)
TIMESTAMP=$(date +%Y%m%d-%H%M%S)
PACKER_DIR="$(dirname "$0")"

# Check inotify-tools
if [[ -z "$INOTIFY_CMD" ]]; then
  echo "Installing inotify-tools..."
  sudo apt update && sudo apt install -y inotify-tools
fi

echo "✅ Watching $LOG_FILE for new package installs..."

while inotifywait -e modify "$LOG_FILE"; do
  if grep -qi "install " "$LOG_FILE"; then
    echo "📦 Detected new package installation!"

    echo "[1/3] Exporting current packages..."
    dpkg --get-selections > "$PACKER_DIR/packages.list"

    echo "[2/3] Triggering Packer build..."
    cd "$PACKER_DIR"
    packer build ami-builder.json

    echo "[3/3] Truncating dpkg log to avoid duplicate triggers..."
    sudo truncate -s 0 "$LOG_FILE"
  fi
done


```
packages.list

```

# This will be auto-generated

```


install_packages.sh

```

#!/bin/bash
set -e

echo "[Provisioner] Updating package list..."
apt update

echo "[Provisioner] Installing packages from list..."
apt install -y $(awk '{print $1}' /tmp/packages.list)

echo "[Provisioner] Cleanup..."
apt clean


```








ami-builder.json

```

{
  "variables": {
    "region": "ap-south-1",
    "source_ami": "ami-0abcdef1234567890",  // Replace with Ubuntu base AMI
    "instance_type": "t3.micro",
    "ami_name": "ubuntu-auto-ami-{{timestamp}}"
  },

  "builders": [{
    "type": "amazon-ebs",
    "region": "{{user `region`}}",
    "source_ami": "{{user `source_ami`}}",
    "instance_type": "{{user `instance_type`}}",
    "ssh_username": "ubuntu",
    "ami_name": "{{user `ami_name`}}"
  }],

  "provisioners": [
    {
      "type": "file",
      "source": "packages.list",
      "destination": "/tmp/packages.list"
    },
    {
      "type": "shell",
      "script": "install_packages.sh"
    }
  ]
}

```



When a new package is installed, the script will:

- Export the full package list

- Call Packer to build a new AMI with the updated packages

- Clear the log to avoid duplicate builds








