#!/bin/bash

db_name=mylocalshop
db_user=wp_shop
db_user_pwd=wp_shop123

cat << EOF
create database $db_name ;

grant all on $db_name.* to $db_user@localhost  identified by '$db_user_pwd';
EOF


