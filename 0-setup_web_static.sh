#!/usr/bin/env bash
# Sets up web servers for the deployment of web_static

set -e

# Install Nginx if it is not already installed
if ! command -v nginx >/dev/null 2>&1; then
    apt-get update
    apt-get install -y nginx
fi

# Create the required directories
mkdir -p /data/web_static/releases/test
mkdir -p /data/web_static/shared

# Create the test HTML file
cat > /data/web_static/releases/test/index.html <<'HTML'
<html>
  <head></head>
  <body>
    School
  </body>
</html>
HTML

# Set directory and file permissions
chmod 755 /data
chmod 755 /data/web_static
chmod 755 /data/web_static/releases
chmod 755 /data/web_static/shared
chmod 755 /data/web_static/releases/test
chmod 644 /data/web_static/releases/test/index.html

# Ensure the required ubuntu user and group exist
if ! getent group ubuntu >/dev/null; then
    groupadd --system ubuntu
fi

if ! id ubuntu >/dev/null 2>&1; then
    useradd --system --gid ubuntu --no-create-home \
        --shell /usr/sbin/nologin ubuntu
fi

# Create the current symbolic link
ln -sfn /data/web_static/releases/test /data/web_static/current

# Set the required ownership after creating all paths
chown -R ubuntu:ubuntu /data
chown -h ubuntu:ubuntu /data/web_static/current
# Configure Nginx to serve the static test page
cat > /etc/nginx/sites-available/default <<'NGINX'
server {
    listen 80 default_server;
    listen [::]:80 default_server;

    root /var/www/html;
    index index.html index.htm;
    server_name _;

    location /hbnb_static/ {
        alias /data/web_static/current/;
        index index.html;
    }

    location = /hbnb_static {
        return 301 /hbnb_static/;
    }
}
NGINX

# Test the configuration and restart or start Nginx
nginx -t

if service nginx status >/dev/null 2>&1; then
    service nginx restart
else
    service nginx start
fi
