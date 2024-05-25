#!/bin/bash
PORT=8080
DEBIAN_FRONTEND=noninteractive
echo Please Authorize This Program
sudo echo Authorized
echo installing Dependencies
rm -f shell2http_1.17.0_linux_amd64.deb
wget https://github.com/msoap/shell2http/releases/download/v1.17.0/shell2http_1.17.0_linux_amd64.deb
sudo dpkg -i shell2http_1.17.0_linux_amd64.deb
echo "Please enter the server directory (make sure its the same directory as server.jar):"
read server_directory
echo "Please enter the server port (default is 25565)"
read server_port
echo Setting up server at port $PORT
shell2http --port $PORT / "cat index.html" /start "sudo java -jar $server_directory/server.jar"