nome=input("Digite o nome: ")
idade=int(input("Digite a idade: "))
prioridade="NÃO"
if idade >=65:
    prioridade="SIM" #se TRUE, irá rodar apenas o que está com TAB
print("O paciente",nome,"possui atendimento prioritário?",prioridade)