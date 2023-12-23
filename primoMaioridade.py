def numIsPrime(numero):
    if numero > 1:
        for i in range(2, numero): #para ver se o numero é divisivel da distancia entre o menor numero primo e ele 
            if numero % i == 0:#comparação entre o indice(i)com o numero passado pelo usuário como parametro 
                return(numero, 'não é primo')
        return(numero, 'é primo')
#elif é else+if simplicado 
    elif numero==0 :
        return("Numero ", numero,"é 0")
    elif numero==1: 
        return("Numero ", numero,"é 1")
    else:
        return("numero inválido")# numeros negativos são invalidos

def verifyAws(resposta, respVerdadeira):
    for answer in respVerdadeira:
        if resposta.lower() in answer.lower(): #verifica independende se for maiusula a resposta do usuário com do sistema permitido 
            return True
    return False

def maioridade(idade):
    if idade>= 18:
        return true #valor True porem em texto para print
    else:
        return false # valor false em texto


repete=True       
while repete==True:

    num=int(input("Digite um numero: "))

    idade= int(input("Digite sua Idade: "))
    print("idade =",maioridade(idade))

    print(numIsPrime(num))

    resp=input("Quer Continuar a verificar mais numeros?[y/n]")
    
    continua=["Sim","Yes", "Y", "S"]#possiveis respostas verdadeiras inseridas pelos usuário

    if verifyAws(resp,continua):#chama a função verifyAws para comparar, se a resposta for true , repete o processo desde o inicio 
        repete=True
        print("\nVamos então.....\n \n")
    else:# sai caso responda false
       print("\nVocê não quer...... então obrigado \n ")
       repete= False







