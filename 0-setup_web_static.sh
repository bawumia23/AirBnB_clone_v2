#!/usr/bin/env bash
# Set up Nginx and the web_static deployment directories

# Install Nginx if it is not already installed
if ! command -v nginx >/dev/null 2>&1; then
    apt-get update
    apt-get install -y nginx
fi

# Create the required directories
mkdir -p /data/web_static/releases/test
mkdir -p /data/web_static/shared

# Create a simple HTML file for testing
cat > /data/web_static/releases/test/index.html <<'HTML'
<!DOCTYPE html>
<html>
  <head>
    <title>Web Static Test</title>
  </head>
  <body>
    <h1>Web Static is working!</h1>
  </body>
</html>
HTML

# Recreate the current symbolic link
rm -rf /data/web_static/current
ln -s /data/web_static/releases/test /data/web_static/current

# Give ubuntu ownership of the entire deployment directory
if id ubuntu >/dev/null 2>&1; then
    chown -R ubuntu:ubuntu /data
else
    chown -R "$(whoami):$(id -gn)" /data
fi
# Configure Nginx to serve the static files
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
}
NGINX

# Test configuration before restarting Nginx
nginx -t && systemctl restart nginx

exit 0
