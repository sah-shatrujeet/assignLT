terraform {
  required_version			 =  ">= 0.12.28"
}

provider "aws" {
  version                    =  "~> 3.0"
  region                     =  "us-east-1"
  shared_credentials_file    =  "/home/shatrujeet/.aws/credentials"
  profile                    =  "default"
}