!#/bin/bash
sudo apt update && sudo apt install nginx
sudo cp -r ~/DraBrIW/* /var/www/html/
sudo service nginx start
