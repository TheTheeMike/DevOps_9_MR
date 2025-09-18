module "nginx_server" {
  source            = "./terraform-nginx"
  vpc_id            = "vpc-0de3c0859746a564a"
  list_of_open_ports = [80, 443, 22]
}

output "server_ip" {
  value = module.nginx_server.instance_public_ip
}