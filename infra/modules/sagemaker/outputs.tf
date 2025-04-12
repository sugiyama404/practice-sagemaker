output "ml_endpoint_name" {
  description = "SageMaker Endpoint Name"
  value       = aws_sagemaker_endpoint.ml_endpoint.name
}
