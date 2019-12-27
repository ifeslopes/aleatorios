import time
num=int(input("entre com numero"))
cont=0
contp=0
while contp<10:
 for i in range(1,num+1):
  	if num%i==0:
  		cont+=1
 if cont==2:
  	print("O numero é primo:\033[35m%d\033[m"%(num))
  	contp+=1
  	cont=0
 else:
  	print("O numero não %d %d" %(num,cont))
 num+=1
 #time.sleep(1)
 cont=0
 
print("O 10°Numero primo\033[35m{}: {}\033[m".format(num-1,contp))
