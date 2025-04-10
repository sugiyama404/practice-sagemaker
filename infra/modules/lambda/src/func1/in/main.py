import boto3
import json
import os
import numpy as np
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    try:
        # SageMakerエンドポイント名を環境変数から取得
        endpoint_name = os.environ.get('ENDPOINT_NAME')

        # サンプル入力データ（イベントからデータを取得するか、サンプルデータを使用）
        if 'data' in event:
            payload = event['data']
        else:
            # サンプルデータ - アヤメの特徴量 (sepal_length, sepal_width, petal_length, petal_width)
            payload = {
                "instances": [
                    [5.1, 3.5, 1.4, 0.2],  # サンプル1
                    [6.7, 3.1, 5.6, 2.4]   # サンプル2
                ]
            }

        # SageMakerランタイムクライアントの初期化
        runtime = boto3.client('runtime.sagemaker')

        # エンドポイントへの推論リクエスト
        logger.info(f"Invoking endpoint: {endpoint_name} with payload: {payload}")
        response = runtime.invoke_endpoint(
            EndpointName=endpoint_name,
            ContentType='application/json',
            Body=json.dumps(payload)
        )

        # レスポンスの処理
        result = json.loads(response['Body'].read().decode())
        logger.info(f"Prediction result: {result}")

        return {
            'statusCode': 200,
            'body': json.dumps({
                'predictions': result
            })
        }
    except Exception as e:
        logger.error(f"Error occurred: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps({
                'error': str(e)
            })
        }
