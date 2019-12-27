from  time import sleep 
n=int(input())
for i in range(0,n):
    sleep(1)
    print(n-i)
    if i==5:
    	print("legal agora é:",n-i)

print('Olá!')