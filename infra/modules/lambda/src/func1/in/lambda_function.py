import boto3
import json

def lambda_handler(event, context):
    client = boto3.client('sagemaker-runtime')
    response = client.invoke_endpoint(
        EndpointName='ml-endpoint',
        Body=json.dumps(event),
        ContentType='application/json'
    )
    result = json.loads(response['Body'].read().decode())
    return {
        'statusCode': 200,
        'body': result
    }
