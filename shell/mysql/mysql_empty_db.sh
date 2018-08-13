#!/bin/ksh

source ../common_ksh/base.ksh

show_command()
{

db_name=$1
db_user=$2

verify db_name
verify db_user

cat <<EOF


CREATE  database $db_name;
CREATE USER '$db_user' IDENTIFIED BY 'Maubant1801';
GRANT ALL PRIVILEGES ON $db_name.*  TO '$db_user'@'%'  IDENTIFIED BY 'Maubant1801';

FLUSH PRIVILEGES;


EOF
}

#-----------------------------
# Main
#-----------------------------
show_command $1 $2

