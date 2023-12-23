nome=input("Digite o nome: ")
idade=int(input("Digite a idade: ")) #Decisões encadeadas são ideais para lidar com várias condições
doenca_infectocontagiosa=input("Suspeita de doença infectocontagiosa?").upper()
if idade >= 65:
    print("Paciente COM prioridade")
    if doenca_infectocontagiosa=="SIM": #"if" dentro de "if"
        print("Encaminhe o paciente para sala AMARELA")
    elif doenca_infectocontagiosa=="NAO":
        print("Encaminhe o paciente para sala BRANCA")
    else:
        print("Responda a suspeita de doença infectocontagiosa com SIM ou NAO")
else:
    print("Paciente SEM prioridade")
    if doenca_infectocontagiosa=="SIM":
        print("Encaminhe o paciente para sala AMARELA")
    elif doenca_infectocontagiosa=="NAO":
        print("Encaminhe o paciente para sala BRANCA")
    else:
        print("Responda a suspeita de doença infectocontagiosa com SIM ou NAO")