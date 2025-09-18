terraform {
  backend "s3" {
    bucket = "terraform-state-danit-devops-9"
    key    = "rmichael/terraform.tfstate"
    region = "eu-central-1"
  }
}