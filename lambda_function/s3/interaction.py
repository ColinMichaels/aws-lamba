import boto3

s3_client = boto3.client('s3')

def download_results_from_s3(s3_path):
    bucket, key = s3_path.replace("s3://", "").split("/", 1)
    response = s3_client.get_object(Bucket=bucket, Key=key)
    return response['Body'].read().decode('utf-8')