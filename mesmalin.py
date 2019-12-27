import time
n=int(input("entre com numero..."))
for i in range(0,n):
    time.sleep(1)
    k=n-i
    print (n-i, end="\r")
    
    if k==10:
    	print("")

print()
print("Ola!")