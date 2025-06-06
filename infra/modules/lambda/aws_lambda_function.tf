# 保護されたエンドポイント用の Lambda 関数
resource "aws_lambda_function" "protected_endpoint" {
  function_name    = "protected_endpoint"
  filename         = data.archive_file.func1.output_path
  handler          = "main.lambda_handler"
  source_code_hash = data.archive_file.func1.output_base64sha256
  role             = var.lambda_iam_role_arn
  runtime          = "python3.12"
  memory_size      = 256

  tags = {
    Name        = "ML-Client-Lambda"
    Environment = "Development"
  }
}
