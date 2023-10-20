import os

def get_aws_credentials():
    # Fetching from environment variables for simplicity. 
    # Production-grade apps might use AWS Secrets Manager.
    return {
        "AWS_ACCESS_KEY": os.environ.get("AWS_ACCESS_KEY"),
        "AWS_SECRET_KEY": os.environ.get("AWS_SECRET_KEY")
    }