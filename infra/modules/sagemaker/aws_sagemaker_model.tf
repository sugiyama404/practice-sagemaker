# 3. SageMaker Model
resource "aws_sagemaker_model" "ml_model" {
  name               = "ml-model-${random_id.suffix.hex}"
  execution_role_arn = var.sagemaker_iam_role_arn

  primary_container {
    image          = "354813040037.dkr.ecr.ap-northeast-1.amazonaws.com/sagemaker-xgboost:1.7-1"
    model_data_url = aws_sagemaker_training_job.training_job.model_artifact_url
  }
  tags = {
    Name        = "ML-Model"
    Environment = "Development"
  }
}
