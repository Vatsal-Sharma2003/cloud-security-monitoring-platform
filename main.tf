provider "aws" {
  region = "ap-south-1"
}

resource "aws_sns_topic" "alerts" {
  name              = "vatsal-alerts"
  kms_master_key_id = "alias/aws/sns"
}

resource "aws_sns_topic_subscription" "email" {
  topic_arn = aws_sns_topic.alerts.arn
  protocol  = "email"
  endpoint  = "vasush3002+aws@gmail.com"
}

resource "aws_iam_role" "lambda_role" {
  name = "lambda_basic_role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Action = "sts:AssumeRole"
      Effect = "Allow"
      Principal = {
        Service = "lambda.amazonaws.com"
      }
    }]
  })
}

resource "aws_iam_role_policy_attachment" "lambda_basic" {
  role       = aws_iam_role.lambda_role.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
}


resource "aws_lambda_function" "alert_lambda" {

  #checkov:skip=CKV_AWS_272: Demo project without code signing
  #checkov:skip=CKV_AWS_116: DLQ intentionally skipped
  #checkov:skip=CKV_AWS_117: VPC intentionally skipped

  function_name = "vatsal-alert-lambda"
  role          = aws_iam_role.lambda_role.arn
  handler       = "index.handler"

  runtime = "python3.13"

  filename         = "lambda.zip"
  source_code_hash = filebase64sha256("lambda.zip")

  reserved_concurrent_executions = 10

  tracing_config {
    mode = "Active"
  }
}

resource "aws_iam_role_policy_attachment" "lambda_sns" {
  role       = aws_iam_role.lambda_role.name
  policy_arn = "arn:aws:iam::aws:policy/AmazonSNSFullAccess"
}
