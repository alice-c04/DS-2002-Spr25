#!/bin/bash
LOCAL_FILE=$1
BUCKET_NAME=$2
EXPIRATION=$3
aws s3 cp "$LOCAL_FILE" "s3://$BUCKET_NAME/" --acl private
FILE_NAME=$(basename "$LOCAL_FILE")
aws s3 presign "s3://$BUCKET_NAME/$FILE_NAME" --expires-in "$EXPIRATION"


