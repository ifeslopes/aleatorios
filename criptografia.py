import random
a="abcdefghijklmnopqrstuvxz"
cri=a+"@*&#%$"
v=str()
while (v !="sair"):
 c=str(input(" entre ?"))
 v=c
 if c=="sair":
 	break
 for i in a:
    for f in c:
    	if f==i:
     	  t=random.choice(cri)
     	  c=c.replace("a",t)
     	  
     	  
 print("letra encontrada", c)
 print("pavra escrita",v)