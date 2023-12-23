resposta="SIM"
while resposta == "SIM":
    nome=input("Digite o nome: ")
    idade=int(input("Digite a idade: "))
    doenca_infectocontagiosa=input("Suspeita de doença infectocontagiosa? ").upper()

    #loop
    while doenca_infectocontagiosa!= "SIM" and doenca_infectocontagiosa!= "NAO": #"!=" simbologia para diferente
        print("Responda apenas com SIM ou NAO")
        doenca_infectocontagiosa = input("Suspeita de doença infectocontagiosa? ").upper()

    #primeiro problema
    if doenca_infectocontagiosa=="SIM":
        print("Encaminhe o paciente para sala AMARELA")
    else:
        print("Encaminhe o paciente para sala BRANCA")

    #segundo problema
    if idade >= 65:
        print("Paciente COM prioridade")
    else:
        genero=input("Digite o gênero do paciente: ").upper()
        if genero=="FEMININO" and idade>10:
            gravidez=input("A paciente está grávida? ").upper()
            if gravidez=="SIM":
                print("Paciente COM prioridade")
            else:
                print("Paciente SEM prioridade")
        else:
            print("Paciente SEM prioridade")

    resposta=input("Deseja repetir o procedimento? (SIM/NAO)").upper()