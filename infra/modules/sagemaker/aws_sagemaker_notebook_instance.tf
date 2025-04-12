resource "aws_sagemaker_notebook_instance" "notebook" {
  name          = "ml-notebook"
  instance_type = "ml.t2.medium"
  role_arn      = var.sagemaker_iam_role_arn
}
