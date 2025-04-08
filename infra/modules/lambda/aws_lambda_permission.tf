# Lambda 関数を API Gateway から呼び出すためのパーミッション
resource "aws_lambda_permission" "api_gateway_lambda" {
  statement_id  = "AllowExecutionFromAPIGateway"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.protected_endpoint.function_name
  principal     = "apigateway.amazonaws.com"
  source_arn    = "${var.apigatewayv2_api_http_api_execution_arn}/*/*"
}

# Lambda オーソライザーを API Gateway から呼び出すためのパーミッション
resource "aws_lambda_permission" "api_gateway_authorizer" {
  statement_id  = "AllowExecutionFromAPIGatewayAuthorizer"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.authorizer.function_name
  principal     = "apigateway.amazonaws.com"
  source_arn    = "${var.apigatewayv2_api_http_api_execution_arn}/authorizers/${var.apigatewayv2_authorizer_lambda_authorizer_id}"
}
