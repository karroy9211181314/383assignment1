import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email = "158120.Moodle@gmail.com"
password = "moodle123"

import os
os.system("sudo apt update")
os.system("sudo apt-get install vim")

os.system("sudo apt install apache2 mysql-client mysql-server php libapache2-mod-php")

os.system("sudo apt install graphviz aspell ghostscript clamav php7.2-pspell php7.2-curl php7.2-gd php7.2-intl php7.2-mysql php7.2-xml php7.2-xmlrpc php7.2-ldap php7.2-zip php7.2-soap php7.2-mbstring")
print("Install Additional Software finished")

os.system("sudo service apache2 restart")

os.system("sudo apt install git")
print("git down;oad finished")

os.system("sudo apt-get install python3-pip")
os.system("sudo pip3 install --upgrade pip")
os.system("sudo pip3 install pymysql")
os.system("sudo pip3 install pandas")
import pymysql



#start
os.chdir("/opt")
os.system("sudo git clone https://github.com/moodle/moodle.git")
os.chdir("/opt/moodle")
os.system("sudo git branch -a")
os.system("sudo git branch -track MOODLE_36_STABLE origin/MOODLE_36_STABLE")
os.system("sudo git checkout MOODLE_36_STABLE ")
print("moodle download finished")

os.system("sudo cp -R /opt/moodle /var/www/html/")
os.system("sudo mkdir /var/moodledata")
os.system("sudo chown -R www-data /var/moodledata")
os.system("sudo chmod -R 777 /var/moodledata")
os.system("chmod -R 0755 /var/www/html/moodle ")

print("copy local repository finished")

#modify mysql configuration file

os.chdir("/etc/mysql/mysql.conf.d/")
#add permission write to the file
os.system("sudo chmod o+w mysqld.cnf ")


data="\ndefault_storage_engine = innodb\ninnodb_file_per_table = 1\ninnodb_file_format = Barracuda"

Sqlfile = open('/etc/mysql/mysql.conf.d/mysqld.cnf',"r")
content = Sqlfile.read()
Sqlfile.close()

position=content.find("skip-external-locking")
length = len("skip-external-locking")
if position != -1:
    content = content[:position+length] + data + content[position+length:]
    Modified_file = open('/etc/mysql/mysql.conf.d/mysqld.cnf',"w")
    Modified_file.write(content)
    Modified_file.close()
    print("the file has been modified")

#change the permission back
os.system("sudo chmod o-w mysqld.cnf ")


#find the top level passwd

os.chdir('/etc/mysql/')
os.system("sudo chmod o+w debian.cnf")
os.system("sudo chmod o+r debian.cnf")

data=""
pwdfile = open('/etc/mysql/debian.cnf',"r")
pwdcontent = pwdfile.read()

pos = pwdcontent.find("[mysql_upgrade]\nhost     = localhost")
lenth=len('[mysql_upgrade]\nhost     = localhost')
UAP=(pwdcontent[pos+lenth:])

pos_user=UAP.find('user     = ')
pos_pwd=UAP.find('password = ')
pos_socket=UAP.find('socket')

TopUser=UAP[pos_user+len('user     = '):pos_pwd].strip()
TopPwd=UAP[pos_pwd+len('password = '):pos_socket].strip()

os.system("sudo chmod o-w debian.cnf")
os.system("sudo chmod o-r debian.cnf")
print("top pwd find finish",TopUser,TopPwd)

# find external ip
r = os.popen("curl ifconfig.me")
ip = r.read()
r.close()

# read the csv file exp file:csv_example new csv file:csv_examples
import csv
import random,string
import pandas as pd
n=10000
num=20
s = string.ascii_lowercase
adr=[]
for i in random.sample(range(1,n),9999):
    if len(str(i))>=4 and len(adr)<num:
        adr.append(str(i)+random.choice(s))
data = pd.read_csv(r'StudentData.csv')
data1  = adr
data['moodle_name'] = data1
data.to_csv(r"StudentDatas.csv",mode = 'a',index =False)



conn = pymysql.connect(host='127.0.0.1',port=3306, user='debian-sys-maint',passwd="lO5k3KdhTU0LoEey")
cursor=conn.cursor()


with open('StudentDatas.csv', 'r') as csvFile:
        reader = csv.reader(csvFile)
        # create empty list
        list_of_students = []
        # for each student, append as list to list (list of lists)
        for row in reader:
                list_of_students.append(row)
                # Remove metadata from top row
        list_of_students.pop(0)


for i in list_of_students:
        SQLcmd1=cursor.execute("create database student%s default character set utf8 collate utf8_general_ci;",i[0])
        SQLcmd3=cursor.execute(" create user student%s@'%%' identified by %s;",(i[0],i[3]))
        SQLcmd4=cursor.execute("GRANT SELECT,INSERT,UPDATE,DELETE,CREATE,CREATE TEMPORARY TABLES,DROP,INDEX,ALTER ON student%s.* TO student%s@'%%' IDENTIFIED BY %s;",(i[0],i[0],i[3]))
        SQLcmd6=cursor.execute("flush privileges;")
conn.commit()
cursor.close()
conn.close()

for i in list_of_students:
        os.system("sudo cp -R /opt/moodle /var/www/html/"+str(i[0]))
        os.chdir("/var/www/html/")
        os.chmod(str(i[0]),777)
        os.chdir(str(i[0]))
        if os.path.isfile("config.php"):
                os.system("rm -rf config.php")

        os.system("touch config.php ")
        data="<?php  // Moodle configuration file\n" \
                "unset($CFG);\n" \
                "global $CFG;\n" \
                "$CFG = new stdClass();\n" \
                "$CFG->dbtype    = 'mysqli';\n" \
                "$CFG->dblibrary = 'native';\n" \
                "$CFG->dbhost    = 'localhost';\n" \
                "$CFG->dbname    = 'student"+str(i[0])+"';\n" \
                "$CFG->dbuser    = 'student"+str(i[0])+"';\n" \
                "$CFG->dbpass    = '"+str(i[3])+"';\n" \
                "$CFG->prefix    = 'mdl_';\n" \
                "$CFG->dboptions = array (\n" \
                "  'dbpersist' => 0,\n" \
                "  'dbport' => '',\n" \
                "  'dbsocket' => '',\n" \
                "  'dbcollation' => 'utf8mb4_unicode_ci',\n" \
                ");\n" \
                "$CFG->wwwroot   = 'http://"+str(ip)+"/"+str(i[4])+"';\n" \
				"$CFG->dataroot  = '/var/moodledata';\n" \
				"$CFG->admin     = 'admin';\n" \
				"$CFG->directorypermissions = 0777;\n" \
				"require_once(__DIR__ . '/lib/setup.php');\n"
        content = data
        file = open('config.php', "w")
        file.write(content)
        file.close()

        #send an email with user login info
        message = MIMEMultipart("alternative")
        message["Subject"] = "Moodle account information"
        message["From"] = sender_email
        message["To"] = str(i[3])


        text = """\
                Subject: Your Login info
        
                Username: """ + 'student'+str(i[0]) + """
                Password: """ + str(i[3]) + """
                Access your Moodle site through this URL: """+'http://'+str(ip)+'/'+str(i[4])

        part1 = MIMEText(text, "plain")
        message.attach(part1)
        # Create secure connection with server and send email
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                server.login(sender_email, password)
                server.sendmail(
                        sender_email, str(i[3]), message.as_string()
        )



os.system("sudo python3 ftp_build.py")
os.system("sudo python3 phpmyadmin.py")
	
		
		
		
