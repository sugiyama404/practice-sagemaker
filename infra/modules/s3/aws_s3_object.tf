resource "aws_s3_object" "training_data" {
  bucket = aws_s3_bucket.ml_data_bucket.bucket
  key    = "train/train.csv"
  source = "${path.module}/src/train.csv"
  etag   = filemd5("${path.module}/src/train.csv")
}
