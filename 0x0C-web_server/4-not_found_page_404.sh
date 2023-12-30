#!/usr/bin/env bash
# configure a new nginx machine to have a custom 404 page
sudo apt-get update
sudo apt-get -y install nginx
sudo ufw allow 'Nginx HTTP'
sudo echo "Hello World!" | sudo tee /var/www/html/index.html
sudo sed -i '/listen 80 default_server/a rewrite ^/redirect_me https://www.youtube.com/ permanent;' /etc/nginx/sites-enabled/default
sudo echo "Ceci n'est pas une page" | sudo tee /var/www/html/404.html
sudo sed -i '/server_name _;/a error_page 404 /404.html;\n\tlocation = /404.html {\n\t\troot /var/www/html;\n\t\tinternal;\n\t}' /etc/nginx/sites-enabled/default
sudo service nginx restart