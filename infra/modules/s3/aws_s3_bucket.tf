# 1. S3 Bucket for Data Management
resource "aws_s3_bucket" "ml_data_bucket" {
  bucket        = "my-ml-data-bucket-${random_string.secret_key.result}"
  force_destroy = true
}

resource "random_string" "secret_key" {
  length  = 20
  upper   = false
  lower   = true
  numeric = true
  special = false
}
