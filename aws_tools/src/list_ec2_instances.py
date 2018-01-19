#!/usr/bin/env python3
# list amazon ec2 instaces

import boto3

# make an object for the client connected to amazon ec2
ec2 = boto3.client('ec2')

# Use the filter() method of the instances collection to retrieve
# all running EC2 instances.
instances = ec2.instances.filter(
    Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
for instance in instances:
    print(instance.id, instance.instance_type)
