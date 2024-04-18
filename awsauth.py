import awscred


def aws_cred():
    AWS_CREDS = {
        "aws_access_key_id": awscred.CLIENT_ID,  # os.getenv("AWS_ACCESS_KEY")
        # os.getenv("AWS_SECRET_KEY")
        "aws_secret_access_key": awscred.CLIENT_SECRET
    }
    return AWS_CREDS
