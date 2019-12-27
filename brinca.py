import  time
n1=-1
n2=1
n3=0
c=0
r=0
f=1
con=0
while c<11:
	print(n3,end='+%d='%(n1))
	n3=n1+n2
	n1=n2
	n2=n3
	c+=1
	for i in range(1,n3+1):
	 	if n3%i==0:
	 		con+=1
	if con==2:
	 	con=0
	 	print('\033[3;31m%d\033[m'%(n3))
	 	r=n3
	 	f=1
	else:
	 	print(n3)
	con=0
	time.sleep(1)
   
		
	while r>0:
	 		
		  print(f,end=' \033[35m%dX%d='%(f,r)if r>1 else ('\n\033[m'))
		  f*=r
		  r-=1
	print()
time.sleep(1)