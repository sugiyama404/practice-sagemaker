resource "aws_lambda_layer_version" "lambda_layer" {
  filename         = "${path.module}/src/func1/my_lambda_layer.zip"
  source_code_hash = filebase64sha256("${path.module}/src/func1/my_lambda_layer.zip")
  layer_name       = "my_lambda_layer"
  description      = "My Lambda Layer"

  compatible_runtimes = ["python3.12"]
}
