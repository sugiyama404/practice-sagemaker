# 保護されたエンドポイント用の Lambda 関数
resource "aws_lambda_function" "protected_endpoint" {
  function_name    = "protected_endpoint"
  filename         = data.archive_file.func1.output_path
  handler          = "main.handler"
  source_code_hash = data.archive_file.func1.output_base64sha256
  role             = var.lambda_authorizer_iam_role_arn
  runtime          = "python3.12"
}

# Lambda オーソライザー関数
resource "aws_lambda_function" "authorizer" {
  function_name    = "api_gateway_authorizer"
  filename         = data.archive_file.func2.output_path
  handler          = "main.handler"
  source_code_hash = data.archive_file.func2.output_base64sha256
  role             = var.lambda_authorizer_iam_role_arn
  runtime          = "python3.12"

  environment {
    variables = {
      AUTH_SECRET = random_string.auth_secret_key.result
    }
  }
}

resource "random_string" "auth_secret_key" {
  length  = 20
  upper   = false
  lower   = true
  numeric = true
  special = false
}
