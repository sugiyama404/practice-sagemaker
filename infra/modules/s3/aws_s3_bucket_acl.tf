resource "aws_s3_bucket_acl" "ml_data_bucket" {
  depends_on = [aws_s3_bucket_ownership_controls.ml_data_bucket]
  bucket     = aws_s3_bucket.ml_data_bucket.id
  acl        = "private"
}
