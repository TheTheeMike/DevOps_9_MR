#!/bin/bash

APP_USER=$1
PROJECT_DIR=$2
REPO_URL=$3
DB_HOST=$4
DB_PORT=$5
DB_NAME=$6
DB_USER=$7
DB_PASS=$8

sudo apt-get update
sudo apt-get install -y openjdk-11-jdk git
app
sudo useradd -m -s /bin/bash "$APP_USER"

sudo -u "$APP_USER" git clone "$REPO_URL" "$PROJECT_DIR"

sudo chown -R "$APP_USER":"$APP_USER" "$PROJECT_DIR"

cd "$PROJECT_DIR/forStep1/PetClinic" 

sudo -u "$APP_USER" chmod +x ./mvnw

sudo -u "$APP_USER" ./mvnw clean package

# Find the jar
JAR_FILE=$(find target -name "*.jar" | head -n 1)
y
APP_HOME="/home/$APP_USER"
sudo cp "$JAR_FILE" "$APP_HOME"
sudo chown "$APP_USER":"$APP_USER" "$APP_HOME/$(basename "$JAR_FILE")"

ENV_FILE="$APP_HOME/app_env.sh"
sudo -u "$APP_USER" bash -c "cat > $ENV_FILE" <<EOF
export DB_HOST=$DB_HOST
export DB_PORT=$DB_PORT
export DB_NAME=$DB_NAME
export DB_USER=$DB_USER
export DB_PASS=$DB_PASS
EOF

sudo chmod +x "$ENV_FILE"
sudo chown "$APP_USER":"$APP_USER" "$ENV_FILE"

sudo -u "$APP_USER" bash -c "source $ENV_FILE && java -jar $APP_HOME/$(basename "$JAR_FILE")" &

#cd mypetclinic/forStep1/PetClinic
#./mvnw package
#java -jar target/*.jar
