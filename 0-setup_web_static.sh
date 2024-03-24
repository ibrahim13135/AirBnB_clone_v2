#!/usr/bin/env bash

# Ensure script is run as root
if [ "$(id -u)" -ne 0 ]; then
    echo "Please run this script with sudo."
    exit 1
fi

apt-get update
apt-get -y install nginx

# Create necessary directories and files
mkdir -p /data/web_static/{releases/test,shared}
echo '<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>' | tee /data/web_static/releases/test/index.html > /dev/null

# Create symbolic link
ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership of the /data/ folder to the www-data user AND group
chown -R www-data:www-data /data/

# Update Nginx configuration
sed -i '/^\tserver_name _;/a \\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}' /etc/nginx/sites-available/default

# Restart Nginx
service nginx restart
