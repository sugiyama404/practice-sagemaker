import boto3
import json
import os

runtime = boto3.client('runtime.sagemaker')
endpoint_name = os.environ['ENDPOINT_NAME']

def lambda_handler(event, context):
    # リクエストデータを準備
    payload = json.dumps(event['data'])

    # SageMakerエンドポイントに予測リクエスト
    response = runtime.invoke_endpoint(
        EndpointName=endpoint_name,
        ContentType='application/json',
        Body=payload
    )

    # レスポンスを解析
    result = json.loads(response['Body'].read().decode())

    return {
        'statusCode': 200,
        'body': json.dumps(result)
    }
