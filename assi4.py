#!/usr/bin/python3
import sys
sys.path.append("H:\\apps\\Python27\\lib\\site-packages")
import cgi
import pymysql
import os
# read the csv file exp file:csv_example new csv file:csv_examples
import csv
import string

import pandas as pd
import pymysql

r = os.popen("curl ifconfig.me")
exip = r.read()
r.close()
f = open("ip.txt","r")
ip = f.read()
f.close() 

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

print("</script>")
for i in list_of_students:
    print("<script type='text/javascript'>")
    print("var btn = document.getElementById('btn')")
    print("btn.onclick=function(){window.location.href='http://'+str(exip)+'/'+str(i[4])+''}")
	print("<tr>")
	print("<td><button id='btn'>student'+str(i[0])+'</button></td>")
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