#!/usr/bin/env python3
# list amazon s3 buckets

import boto3

# make s3 object
s3 = boto3.resource('s3')

# enumerate list of buckets
for bucket in s3.buckets.all():
    print(bucket.name)
