#!/bin/bash

db_name=shop_db
db_user=admin
db_user_pwd=admin123

cat << EOF
create database $db_name ;

grant all on $db_name.* to $db_user@localhost  identified by '$db_user_pwd';
EOF


step_for_wordpress()
{

cat << EOF



sudo cd /var/www/html
sudo tar -xvf latest.tar

sudo chown -R www-data.www-data wordpress

cd wordpress
sudo cp wp-config-sample.php wp-config.php

open below link
	http://192.168.1.42/wordpress/wp-admin/install.php


EOF

}


step_for_wordpress

