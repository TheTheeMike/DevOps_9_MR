#!/bin/bash

DB_USER=$1
DB_PASS=$2
DB_NAME=$3

sudo apt-get update
sudo apt-get install -y mysql-server

sudo sed -i "s/^bind-address.*/bind-address = 192.168.56.2/" /etc/mysql/mysql.conf.d/mysqld.cnf

sudo systemctl restart mysql

mysql -u root <<MYSQL_SCRIPT
CREATE DATABASE IF NOT EXISTS ${DB_NAME};
CREATE USER IF NOT EXISTS '${DB_USER}'@'192.168.56.%' IDENTIFIED BY '${DB_PASS}';
GRANT ALL PRIVILEGES ON ${DB_NAME}.* TO '${DB_USER}'@'192.168.56.%';
FLUSH PRIVILEGES;
MYSQL_SCRIPT

echo "MySQL setup complete with DB_NAME=${DB_NAME}, DB_USER=${DB_USER}"