import boto3
from awsauth import aws_cred
from awscred import SECURE_SECRET


class SecretManager:
    def __init__(self, region) -> None:
        self.secretmanagerclient = boto3.client(
            'secretsmanager', **aws_cred(), region_name=region)

    def listsecrets(self):
        response = self.secretmanagerclient.list_secrets()
        return response

    def getsecretname(self):
        response = self.secretmanagerclient.list_secrets(
            Filters=[
                {
                    'Key': 'Name',
                    'Values': ['awssecretva']

                }
            ]

        )
        return response

    def createsecret(self):
        response = self.secretmanagerclient.create_secret(
            Name='awssecretva',
            Description='for further uses',
            # KmsKeyId='string',
            # SecretBinary=b'bytes',
            SecretString=SECURE_SECRET,
            Tags=[
                {
                    'Key': 'env',
                    'Value': 'int'
                },
            ],
        )
        return response['SecretList']['Name']

    def getsecretvalue(self):
        response = self.secretmanagerclient.get_secret_value(
            SecretId='awssecretva'
        )
        return response['SecretString']
