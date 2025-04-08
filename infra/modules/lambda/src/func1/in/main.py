# ファイル名: protected_endpoint/main.py
# ZIP形式で圧縮し、TerraformのLambdaリソースで指定

import json
import logging
import os
import datetime

# ロガーの設定
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def handler(event, context):
    """
    保護されたAPIエンドポイントのハンドラー関数
    認証済みユーザーからのリクエストを処理し、レスポンスを返します

    Args:
        event (dict): API Gateway からのイベントデータ
        context (object): Lambda コンテキスト情報

    Returns:
        dict: HTTP レスポンス
    """
    # リクエスト情報のログ記録（機密情報は除外）
    request_data = {
        "path": event.get("path"),
        "httpMethod": event.get("httpMethod"),
        "requestId": event.get("requestContext", {}).get("requestId"),
        "sourceIp": event.get("requestContext", {}).get("http", {}).get("sourceIp")
    }
    logger.info(f"Request received: {json.dumps(request_data)}")

    try:
        # オーソライザーから渡されたコンテキスト情報の取得
        auth_context = event.get('requestContext', {}).get('authorizer', {})
        principal_id = auth_context.get('principalId', 'unknown')

        # コンテキストから追加情報を取得（存在する場合）
        context_data = {
            "stringKey": auth_context.get('stringKey', ''),
            "numberKey": auth_context.get('numberKey', 0),
            "booleanKey": auth_context.get('booleanKey', False)
        }

        # 現在の日時
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # レスポンスデータの作成
        response_data = {
            "message": "認証成功！保護されたリソースにアクセスできました",
            "principalId": principal_id,
            "timestamp": current_time,
            "region": os.environ.get("AWS_REGION", "不明"),
            "authContext": context_data
        }

        # クエリパラメータがある場合は追加
        query_params = event.get('queryStringParameters')
        if query_params:
            response_data["queryParams"] = query_params

        # 正常なレスポンスを返す
        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*",  # CORS設定
                "Access-Control-Allow-Methods": "GET,OPTIONS",
                "Access-Control-Allow-Headers": "Content-Type,Authorization"
            },
            "body": json.dumps(response_data, ensure_ascii=False)
        }

    except Exception as e:
        # エラーログの記録
        logger.error(f"Error processing request: {str(e)}", exc_info=True)

        # エラーレスポンスを返す
        return {
            "statusCode": 500,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*"
            },
            "body": json.dumps({
                "message": "内部サーバーエラーが発生しました",
                "errorType": type(e).__name__
            }, ensure_ascii=False)
        }
