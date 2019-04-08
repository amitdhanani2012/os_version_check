#!/root/fabric_test/bin/python2.7
from fabric import Connection
import csv
j=[]
for i in open("server1.txt","r"):
    j.append(i.strip())
print(j)



wr1=open('output1.csv','a')
writer1=csv.writer(wr1)

for k in j:
   result=None
   l=None
   x=None
   y=None
   print(k) 
   o=str(k)
   c = Connection(o,user="hyperic",connect_kwargs={"password": "testing"})
 
   result=c.run("hostname")
   print("my result.............")
   l=result.stdout.split("\r\n")
   print(l[0])

   result=c.run('uname -a')
   print("my result.............")
   x=result.stdout.split("\r\n")
   print(x[0])

   try: 
        result=c.run('cat /etc/redhat-release')
   except:
        y=['not redhat']
   else:
   	y=result.stdout.split("\r\n")
   	print(y[0])
   	print(".............................")
   
   writer1.writerow((l[0],k,x[0],y[0]))
wr1.close()
