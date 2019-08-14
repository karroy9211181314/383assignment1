import random,string,csv
n=10000
num=20
s = string.ascii_lowercase
adr=[]
for i in random.sample(range(1,n),2000):
    if len(str(i))>=4 and len(adr)<num:
        adr.append(str(i)+random.choice(s))
import pandas as pd
data = pd.read_csv(r'csv_example.csv')
data1  = adr
data['moodle_name'] = data1
data.to_csv(r"csv_examples.csv",mode = 'a',index =False)
with open('csv_examples.csv', 'r') as csvFile:
    reader = csv.reader(csvFile)
    list_of_students = []
    for row in reader:
        list_of_students.append(row)
    list_of_students.pop(0)
