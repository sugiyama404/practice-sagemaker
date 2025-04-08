resource "aws_s3_bucket_ownership_controls" "ml_data_bucket" {
  bucket = aws_s3_bucket.ml_data_bucket.id
  rule {
    object_ownership = "BucketOwnerPreferred"
  }
}
