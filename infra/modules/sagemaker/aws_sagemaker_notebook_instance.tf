# 2. SageMaker Notebook Instance
resource "aws_sagemaker_notebook_instance" "ml_notebook" {
  name          = "ml-development-notebook-${random_id.suffix.hex}"
  role_arn      = aws_iam_role.sagemaker_role.arn
  instance_type = "ml.t2.medium"

  # Optional: Lifecycle configuration script
  lifecycle_config_name = aws_sagemaker_notebook_instance_lifecycle_configuration.ml_notebook_config.name
}
