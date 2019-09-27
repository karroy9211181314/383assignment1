#!/usr/bin/python
import sys
import os
sys.path.append("H:\\apps\\Python27\\lib\\site-packages")
import cgi




import csv
import random,string

os.system("sudo pip3 install pandas")
print("panas install finished")

import pandas as pd
import pymysql

r = os.popen("curl ifconfig.me")
ip = r.read()
r.close()
with open('StudentData.csv', 'r') as csvFile:
        reader = csv.reader(csvFile)
        # create empty list
        list_of_students = []
        # for each student, append as list to list (list of lists)
        for row in reader:
                list_of_students.append(row)
                # Remove metadata from top row
        list_of_students.pop(0)
n=10000
m=1000000
num=len(list_of_students)
s = string.ascii_lowercase
adr=[]
pas=[]
for i in random.sample(range(1,n),n-1):
    if len(str(i))>=4 and len(adr)<num:
        adr.append(str(i)+random.choice(s))
for i in random.sample(range(1,m),m-1):
    if len(str(i))>=6 and len(pas)<num:
        pas.append(str(i))
data = pd.read_csv(r'StudentData.csv')
data1 = adr
data2 = pas
data['moodle_name'] = data1
data['password'] = data2
data.to_csv(r"StudentDatas.csv",mode = 'a',index =False)

with open('StudentDatas.csv', 'r') as csvFile:
        reader = csv.reader(csvFile)
        # create empty list
        list_of_students = []
        # for each student, append as list to list (list of lists)
        for row in reader:
                list_of_students.append(row)
                # Remove metadata from top row
        list_of_students.pop(0)







print("Content-type: text/html\n")
print("<title>Assignment4 progress</title>")
print("<head>")
print("<style type='text/css'>")
print("th,td{border:2px solid black;}")
print("table{padding: 60px 50px;}")
print("input:hover { background-color:green; /* Green */    color: white;border-radius: 50%;}")
print("input {color: green; text-align: left; text-decoration: none; display: inline-block; font-size: 1
6px;border: 2px solid #4CAF50;border-radius: 50%;}")
print("body {background:url('http://blog.hostbaby.com/wp-content/uploads/2014/03/PaintSquares_1400x900-1
024x658.jpg');background-size:98% 100%;background-repeat:no-repeat; }")
print("h1{text-shadow: 5px 5px 5px #95CACA;text-align:center;text-decoration:overline;letter-spacing:2px
;")
print("</style>")
print("</head>")
print("<body><center>")
print("<h1>Progress of Assignment4</h1>")
print("<table>")
print("<tr><th>ID/task</th><th>first</th><th>second</th></tr>")
for i in list_of_students:
	print("<tr>")
	print("<td><a href='http://"+str(ip)+"/"+str(i[4])+"'>student"+str(i[0])+"</a></td>")
	# get post data
	form = cgi.FieldStorage()
	os.system("cd /var/www/html/"+str(i[4])+"")
	firstfile=os.system("find . -name 'php_echo.php'")
	if firstfile==1:
		print("<th>yes</th>")
	else:
		print("<th>no</th>")
	os.system("cd /var/www/html/"+str(i[4])+"/course")
	secfile=os.system("find . -name 'view_mod.php'")
	if secfile ==1:
		print("<th>ok</th>")
	else:
		print("<th>no</th>")
print("</tr></table>")
print("""
<form action="../login.html" method="GET">
    <input type="submit" value="Back to progress">
</form>
""")
print('</center></body>')