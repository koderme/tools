sudo apt install mongodb

sudo systemctl enable mongodb	
sudo systemctl disable mongodb	

sudo systemctl restart mongodb
sudo systemctl status mongodb


# Allow access from everywhere
sudo ufw allow 27017


#--------------------------------------------------
# Create MongoDB Database Root User and Password
#--------------------------------------------------

1.      mongo      # For launching mongo shell
2.      show dbs   # show dbs
3.      use admin  # switch to admin db
4.      db.createUser({user:"root", pwd:"=root123", roles:[{role:"root", db:"admin"}]})

5  sudo vim /lib/systemd/system/mongodb.service
   change below command 
	ExecStart=/usr/bin/mongod --unixSocketPrefix=${SOCKETPATH} --config ${CONF} $DAEMON_OPTS

	to

	ExecStart=/usr/bin/mongod --auth --unixSocketPrefix=${SOCKETPATH} --config ${CONF} $DAEMON_OPTS


6  Run below commands

    $ systemctl daemon-reload
    $ sudo systemctl restart mongodb	
    $ sudo systemctl status mongodb	


#--------------------------------------------------
# Change password
#--------------------------------------------------
mongo -u "root" -p --authenticationDatabase "admin"

use admin
db.changeUserPassword("root", "root123")



