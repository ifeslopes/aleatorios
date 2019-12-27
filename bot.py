i=0
v=""
m=int()
j=str(input('Por vavor qual é o seu nome?'))
while (v!='sai'):
	i+=1
	a=int(input("Então %s...Digite qualquer numero ai? "%j))
	#m=int()
	if m<a:
		
		print("O %s, numero %d é maior que %d "%(j,a,m))
		m=a
	
	if i==1:
		print("fala ai %s, meu brothe, vou jorgar valor de %d em M para calcular o menor numero beleza "%(j,a))
	if m>a:
		
		print("O numero%d é maior que%d"%(m,a))
		m=a

	v=input("Digite:(Sair) para encerra o programa")
		