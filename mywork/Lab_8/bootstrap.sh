#!/bin/bash 
/usr/bin/yum update -y
/bin/amazon-linux-extras install -y epel
/usr/bin/yum install -y git python3 python3-dev python3-pip nfs-utils
/bin/pip3 install boto3 pandas requests
