import boto3
from urllib.parse import unquote_plus

# Create a new S3 resource
s3_client = boto3.client('s3')

dynamodb_client = boto3.client(service_name='dynamodb', endpoint_url='http://localhost:8000')

def lambda_handler(event, context):
    print('Debug: Hello')
    print(event)
    for record in event['Records']:
        print(record)
        bucket = record['s3']['bucket']['name']
        print(bucket)
        key = unquote_plus(record['s3']['object']['key'])
        print(key)
