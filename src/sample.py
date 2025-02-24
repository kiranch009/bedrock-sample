import boto3


bedrock_client = boto3.client('bedrock')

def execute():
    print('Hello, World!')