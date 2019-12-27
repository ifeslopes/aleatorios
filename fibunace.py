v1=-1
v2=1
v3=0
for i in range(1,15+1):
	v3=v1+v2
	v1=v2
	v2=v3
	print(v3)