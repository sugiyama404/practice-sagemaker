# 4. SageMaker Endpoint Configuration
resource "aws_sagemaker_endpoint_configuration" "ml_endpoint_config" {
  name = "ml-endpoint-config-${random_id.suffix.hex}"

  production_variants {
    variant_name           = "default"
    model_name             = aws_sagemaker_model.ml_model.name
    instance_type          = "ml.t2.medium"
    initial_instance_count = 1
  }
}
