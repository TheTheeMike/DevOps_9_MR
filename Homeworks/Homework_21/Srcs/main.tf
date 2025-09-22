
provider "aws" {
  region = "eu-central-1"
}

resource "aws_key_pair" "my_key" {
  key_name   = "my-key"
  public_key = file("~/.ssh/id_rsa.pub")
}

resource "aws_security_group" "allow_ssh_http" {
  name        = "allow_ssh_http"
  description = "Allow SSH and HTTP"

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_instance" "web" {
  count         = 2
  ami           = "ami-0a116fa7c861dd5f9"
  instance_type = "t2.micro"
  key_name      = aws_key_pair.my_key.key_name
  security_groups = [aws_security_group.allow_ssh_http.name]

  tags = {
    Name = "Terraform-Ansible-${count.index + 1}"
  }
}

resource "null_resource" "generate_inventory" {
  depends_on = [aws_instance.web]

  provisioner "local-exec" {
    command = <<EOT
echo "[web]" > inventory.ini
for ip in ${join(" ", aws_instance.web[*].public_ip)}; do
  echo "$ip ansible_user=ubuntu ansible_ssh_private_key_file=~/.ssh/id_rsa" >> inventory.ini
done
EOT
  }
}

output "instance_ips" {
  value = aws_instance.web[*].public_ip
}
