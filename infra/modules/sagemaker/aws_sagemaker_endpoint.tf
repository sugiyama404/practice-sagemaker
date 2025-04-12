# 5. SageMaker Endpoint
resource "aws_sagemaker_endpoint" "ml_endpoint" {
  name                 = "ml-endpoint"
  endpoint_config_name = aws_sagemaker_endpoint_configuration.ml_endpoint_config.name
}
