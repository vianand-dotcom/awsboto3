import boto3
from awsauth import aws_cred
from awsec2 import AwsEc2
from awssecretmanager import SecretManager


def aws_s3bucket():
    s3 = boto3.client('s3', **aws_cred())
    response = s3.list_buckets()
    return response


def aws_ec2instance(region):
    ec2 = boto3.client('ec2', **aws_cred(), region_name=region)
    # response = ec2.describe_regions()
    # response = ec2.describe_instances()
    # response = ec2.describe_instance_attribute("awsec2deva")
    response = ec2.start_instances(InstanceIds=["i-05b9eebcbd92bcd2a"])
    # response = ec2.list_instances()

    return response


aws_region = "us-east-1"
print(aws_s3bucket())
print("----ec2 instance listing-------")
ec2inst = AwsEc2(aws_region)
print(ec2inst.ec2_startinstance(instanceid="t1"))
# print(aws_ec2instance("us-east-1"))
print("----secret listing-------")
secmaninst = SecretManager(aws_region)
print(secmaninst.listsecrets())
# print(secmaninst.createsecret())
print("-----get secret value----")
print(secmaninst.getsecretvalue())
print("----list secret if exist")
print(secmaninst.listsecrets())
