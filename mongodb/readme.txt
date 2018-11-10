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
# Login
#--------------------------------------------------
mongo -u "root" -p --authenticationDatabase "admin"
mongo -u "vishal" -p --authenticationDatabase "resim"

use admin
db.changeUserPassword("root", "root123")

#--------------------------------------------------
# Create user
#--------------------------------------------------
 db.createUser( { user: "vishal", pwd: "vishal", roles: [ "readWrite", "dbOwner"] })
 db.createUser( { user: "vishal", pwd: "vishal", roles: [ "userAdminAnyDatabase" ] })
 db.createUser( { user: "vishal", pwd: "vishal", roles: [ { role: "root", db: "ecomm" } ] })
 db.createUser( { user: "vishal", pwd: "vishal", roles: [ { role: "readWrite", db: "resim" } ] })

dbOwner 

use admin
db.changeUserPassword("root", "root123")

#--------------------------------------------------
# Create user
#--------------------------------------------------
 [1] Login as "root" into "admin"
 [2] Create user
    db.createUser( { user: "u1", pwd: "password", roles: [ { role: "readWrite", db: "db1" } ] })

 [3] Logout 
 [4] Login as "u1" into "db1"
 [5] Change the db to "db1"
     use db1
 
#--------------------------------------------------
# collection (table)
#--------------------------------------------------
db.createCollection("emp")           ### create collection
db.dept.insert({"deptno" : "100"})   ### coll is created automatically row is inserted

show collections   ### display all collections

db.emp.drop()      ### drop collection



#--------------------------------------------------
# documnet (row)
#--------------------------------------------------
db.emp.insert({
   name: 'John White', 
   empno: '100',
   colors: ['red', 'orange', 'blue'],
   salary: 10000
})


db.emp.find()           ### show all documents
db.emp.find().pretty()  ### show all documents formatted
