#!/usr/bin/env bash
# Sets up web servers for the deployment of web_static

# Install Nginx if not already installed
if ! command -v nginx &> /dev/null; then
    apt-get update
    apt-get install -y nginx
fi

# Create required folders
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/

# Create a fake HTML file for testing
echo "<html>
  <head>
  </head>
  <body>
    School
  </body>
</html>" > /data/web_static/releases/test/index.html

# Create or recreate the symbolic link
if [ -L /data/web_static/current ]; then
    rm /data/web_static/current
fi
ln -s /data/web_static/releases/test/ /data/web_static/current

# Give recursive ownership of /data/ to ubuntu user and group
if id "ubuntu" &>/dev/null; then
    chown -R ubuntu:ubuntu /data/
else
    useradd -m ubuntu
    chown -R ubuntu:ubuntu /data/
fi

# Update Nginx configuration to serve /data/web_static/current/ at /hbnb_static
nginx_config="server {
    listen 80 default_server;
    listen [::]:80 default_server;

    root /var/www/html;
    index index.html index.htm index.nginx-debian.html;

    server_name _;

    location /hbnb_static {
        alias /data/web_static/current/;
        index index.html index.htm;
    }
}"

echo "$nginx_config" > /etc/nginx/sites-available/default

# Restart Nginx
service nginx restart
