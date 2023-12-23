tabuada=int(input("Insira um número para fazer a tabuada: "))
for valor in range(1,11,1): #vai criar uma lista começando com 1, terminando em 11, de 1 em 1 > "1,11,1"
    print("\t",str(tabuada), "x",str(valor),"=",tabuada*valor)
#ao atingir o 11, ele encerra o laço e não exibe a informação