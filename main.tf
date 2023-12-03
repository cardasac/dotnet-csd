resource "aws_elastic_beanstalk_application" "csd" {
  name        = "csd"
  description = "Main app"
}

variable "sentry_dns" {
  type      = string
  sensitive = true
}

locals {
  common_settings = [
    {
      namespace = "aws:elasticbeanstalk:environment"
      name      = "ServiceRole"
      value     = "aws-elasticbeanstalk-service-role"
    },
    {
      namespace = "aws:elasticbeanstalk:environment"
      name      = "LoadBalancerType"
      value     = "application"
    },
    {
      namespace = "aws:autoscaling:launchconfiguration"
      name      = "IamInstanceProfile"
      value     = "aws-elasticbeanstalk-ec2-role"
    },
    {
      namespace = "aws:ec2:instances"
      name      = "SupportedArchitectures"
      value     = "arm64"
    },
    {
      namespace = "aws:ec2:instances"
      name      = "InstanceTypes"
      value     = "t4g.micro"
    }
  ]

  environment_settings = {
    staging = [
      {
        namespace = "aws:elasticbeanstalk:application:environment"
        name      = "SENTRY_DNS"
        value     = var.sentry_dns
      },
      {
        namespace = "aws:elasticbeanstalk:application:environment"
        name      = "SENTRY_ENVIRONMENT"
        value     = "staging"
      }
    ],
    production = [
      {
        namespace = "aws:elasticbeanstalk:command"
        name      = "DeploymentPolicy"
        value     = "Immutable"
      },
      {
        namespace = "aws:elasticbeanstalk:application:environment"
        name      = "SENTRY_ENVIRONMENT"
        value     = "production"
      }
    ]
  }
}

resource "aws_elastic_beanstalk_environment" "staging" {
  name                = "staging"
  application         = aws_elastic_beanstalk_application.csd.name
  solution_stack_name = "64bit Amazon Linux 2023 v4.0.6 running Python 3.11"
  cname_prefix        = "csd-staging"

  dynamic "setting" {
    for_each = concat(local.common_settings, local.environment_settings.staging)
    content {
      namespace = setting.value["namespace"]
      name      = setting.value["name"]
      value     = setting.value["value"]
    }
  }
}

resource "aws_elastic_beanstalk_environment" "production" {
  name                = "production"
  application         = aws_elastic_beanstalk_application.csd.name
  solution_stack_name = "64bit Amazon Linux 2023 v4.0.6 running Python 3.11"
  cname_prefix        = "csd-production"

  dynamic "setting" {
    for_each = concat(local.common_settings, local.environment_settings.production)
    content {
      namespace = setting.value["namespace"]
      name      = setting.value["name"]
      value     = setting.value["value"]
    }
  }
}
