# 3. SageMaker Model
resource "aws_sagemaker_model" "ml_model" {
  name               = "ml-model-${random_id.suffix.hex}"
  execution_role_arn = aws_iam_role.sagemaker_role.arn

  primary_container {
    image          = "763104351884.dkr.ecr.us-east-1.amazonaws.com/tensorflow-training:2.9.1-cpu-py39-ubuntu20.04-e3"
    model_data_url = "s3://${aws_s3_bucket.ml_data_bucket.bucket}/models/model.tar.gz"
  }
}
