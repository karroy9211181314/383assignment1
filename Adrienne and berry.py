import os
import pymysql
import csv
# read the csv file
with open('C:\\Users\\adrienne\\Desktop\\csv_example.csv', 'r') as csvFile:
    reader = csv.reader(csvFile)
    list_of_students = []
    for row in reader:
        list_of_students.append(row)
    list_of_students.pop(0)
csvFile.close()
# finish downing moodle
os.chdir("/opt")
os.system("sudo git clone https://github.com/moodle/moodle.git")
os.chdir("/opt/moodle")
os.system("sudo git branch -a")
os.system("sudo git branch -track MOODLE_36_STABLE origin/MOODLE_36_STABLE")
os.system("sudo git checkout MOODLE_36_STABLE ")
print("moodle download finished")

TopUser  = 'debian-sys-maint'
TopPwd = '0A7XW7QUpbRYhllT'

# create users databases and the moodle account
conn = pymysql.connect(host='127.0.0.1',port=3306, user=TopUser,passwd=TopPwd)
cursor=conn.cursor()

for i in list_of_students:
	SQLcmd1=cursor.execute("create database ID%s default character set utf8 collate utf8_general_ci;",i[0])
	SQLcmd3=cursor.execute(" create user ID%s@'%%' identified by %s;",(i[0],i[3]))
	SQLcmd4=cursor.execute("GRANT SELECT,INSERT,UPDATE,DELETE,CREATE,CREATE TEMPORARY TABLES,DROP,INDEX,ALTER ON ID%s.* TO ID%s@'%%' IDENTIFIED BY %s;",(i[0],i[0],i[3]))
	SQLcmd6=cursor.execute("flush privileges;")
conn.commit()
cursor.close()
conn.close()
os.system("sudo mkdir /var/moodledata")
for i in list_of_students:
	os.system("sudo cp -R /opt/moodle /var/www/html/ID%s",i[0])
	os.system("sudo chown -R www-data /var/moodledata")
	os.system("sudo chmod -R 777 /var/moodledata")
	os.system("chmod -R 777 /var/www/html/ID%s ",i[0])
	os.system("sudo cd /var/www/html/ID%s",i[0])
	if os.path.isfile("config.php"):
		os.system("sudo rm-rf config.php")
	os.system("touch config.php ")
	data=("<?php  // Moodle configuration file\n" \
		 "unset($CFG);\n" \
		 "global $CFG;\n" \
		 "$CFG = new stdClass();\n" \
		 "$CFG->dbtype    = 'mysqli';\n" \
		 "$CFG->dblibrary = 'native';\n" \
		 "$CFG->dbhost    = 'localhost';\n" \
		 "$CFG->dbname    = 'ID%s';\n" \
		 "$CFG->dbuser    = 'ID%s';\n" \
		 "$CFG->dbpass    = %s;\n" \
		 "$CFG->prefix    = 'mdl_';\n" \
		 "$CFG->dboptions = array (\n" \
		 "  'dbpersist' => 0,\n" \
		 "  'dbport' => '',\n" \
		 "  'dbsocket' => '',\n" \
		 "  'dbcollation' => 'utf8mb4_unicode_ci',\n" \
		 ");\n" \
		 "$CFG->wwwroot   = 'http://%s/moodle';\n" \
		 "$CFG->dataroot  = '/var/moodledata';\n" \
		 "$CFG->admin     = 'admin';\n" \
		 "$CFG->directorypermissions = 0777;\n" \
		 "require_once(__DIR__ . '/lib/setup.php');\n",i[0],i[0],i[3],i[0])
	content=data
	file = open('config.php',"w")
	file.write(content)
	file.close()

