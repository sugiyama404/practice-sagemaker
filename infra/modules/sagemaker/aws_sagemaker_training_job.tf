# SageMaker Training Job
resource "aws_sagemaker_training_job" "training_job" {
  training_job_name = "training-job-${random_id.suffix.hex}"
  role_arn          = aws_iam_role.sagemaker_role.arn

  algorithm_specification {
    training_image      = "354813040037.dkr.ecr.ap-northeast-1.amazonaws.com/sagemaker-xgboost:1.7-1"
    training_input_mode = "File"
  }

  hyper_parameters = {
    "max_depth" = "3"
    "eta"       = "0.1"
    "objective" = "binary:logistic"
    "num_round" = "10"
  }

  input_data_config {
    channel_name = "train"
    data_source {
      s3_data_source {
        s3_data_type = "S3Prefix"
        s3_uri       = "s3://${var.s3-ml-data-bucket}/data/"
      }
    }
  }

  output_data_config {
    s3_output_path = "s3://${var.s3-ml-data-bucket}/output/"
  }

  resource_config {
    instance_count    = 1
    instance_type     = "ml.m5.large"
    volume_size_in_gb = 5
  }

  stopping_condition {
    max_runtime_in_seconds = 3600
  }

  tags = {
    Name        = "ML-Training-Job"
    Environment = "Development"
  }
}
