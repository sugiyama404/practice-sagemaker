# 1. S3 Bucket for Data Management
resource "aws_s3_bucket" "ml_data_bucket" {
  bucket        = "my-ml-data-bucket-1234543245422"
  force_destroy = true
}
