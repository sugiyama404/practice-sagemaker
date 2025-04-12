import boto3
import json

# boto3 の SageMaker Runtime クライアントを初期化
sagemaker_runtime = boto3.client("sagemaker-runtime")

def lambda_handler(event, context):
    # 入力データ（例：event 経由で渡される JSON 形式のデータ）
    input_data = json.dumps(event.get("data", {}))

    try:
        # SageMaker エンドポイントを呼び出し
        response = sagemaker_runtime.invoke_endpoint(
            EndpointName="ml-endpoint",  # Terraformで作成したエンドポイント名に合わせて
            ContentType="application/json",
            Body=input_data
        )

        result = response["Body"].read().decode("utf-8")
        return {
            "statusCode": 200,
            "body": json.loads(result)
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "error": str(e)
        }
