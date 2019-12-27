print("Tabela ASCII de 32 a 127: ")
for i in range(32,128, 3):
	print("ASCII [ %2d ] = '%s'ASCII[ %2d] = '%s'\nASCII[ %2d ] = '%s'\n"%(i, chr(i), i+1,chr(i+1), i+2 ,chr(i+2)),end="")