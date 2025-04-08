# ファイル名: lambda_authorizer/main.py
# ZIP形式で圧縮し、TerraformのLambdaリソースで指定

import json
import os
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def handler(event, context):
    logger.info(f"Event: {json.dumps(event)}")

    try:
        # Authorizationヘッダーから認証トークンを取得
        headers = event.get('headers', {})
        auth_header = headers.get('authorization') or headers.get('Authorization')

        if not auth_header:
            logger.warning("No Authorization header found")
            return generate_policy('user', 'Deny', event.get('routeArn', '*'))

        # ここに実際の認証ロジックを実装
        # 例: Bearer tokenの検証、JWTの検証など
        if auth_header.startswith('Bearer '):
            token = auth_header[7:]  # 'Bearer ' の後の部分を取得

            # トークン検証ロジック（この例では簡易的な検証）
            if token == os.environ.get('AUTH_SECRET'):
                logger.info("Authentication successful")
                return generate_policy('user', 'Allow', event.get('routeArn', '*'))

        logger.warning("Authentication failed")
        return generate_policy('user', 'Deny', event.get('routeArn', '*'))

    except Exception as e:
        logger.error(f"Error: {str(e)}")
        return generate_policy('user', 'Deny', event.get('routeArn', '*'))

# HTTP API用のシンプルなレスポンス形式のポリシー生成関数
def generate_policy(principal_id, effect, resource):
    return {
        "isAuthorized": effect == 'Allow',
        "context": {
            "principalId": principal_id,
            # 追加のコンテキスト情報を必要に応じて含めることができます
            "stringKey": "string value",
            "numberKey": 123,
            "booleanKey": True
        }
    }
