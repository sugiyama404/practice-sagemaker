resource "aws_s3_object" "sample_data" {
  bucket     = aws_s3_bucket.ml_data_bucket.bucket
  key        = "data/sample_data.csv"
  source     = local_file.sample_data.filename
  etag       = filemd5(local_file.sample_data.filename)
  depends_on = [local_file.sample_data]
}

resource "aws_s3_object" "train_script" {
  bucket     = aws_s3_bucket.ml_data_bucket.bucket
  key        = "code/train.py"
  source     = local_file.train_script.filename
  etag       = filemd5(local_file.train_script.filename)
  depends_on = [local_file.train_script]
}

# CSVファイルのローカル配置
resource "local_file" "sample_data" {
  content  = file("${path.module}/src/sample_data.csv")
  filename = "${path.module}/src/sample_data.csv"
}

# トレーニングスクリプトのローカル配置
resource "local_file" "train_script" {
  content  = file("${path.module}/src/train.py")
  filename = "${path.module}/src/train.py"
}
