import boto3
from awsauth import aws_cred


class AwsEc2:
    def __init__(self, region):
        self.ec2 = boto3.client('ec2', **aws_cred(), region_name=region)

    def ec2_describeinstances(self):
        response = self.ec2.describe_instances()
        return response

    def ec2_startinstance(self, instanceid):
        response = self.ec2.start_instances(
            InstanceIds=["i-05b9eebcbd92bcd2a"])
        return response
