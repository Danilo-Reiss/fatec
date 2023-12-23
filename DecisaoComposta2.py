nome=input("Digite o nome: ")
idade=int(input("Digite a idade: "))
doenca_infectocontagiosa=input("Suspeita de doença infecto-contagiosa?").upper() #atribui caixa alta
if idade>=65:
    print("O paciente ",nome, " POSSUI atendimento prioritário!")
elif doenca_infectocontagiosa=="SIM": # "=">Atribuição;"==">Comparação; "elif">Segunda condição
    print("O paciente " + nome + " deve ser direcionado para sala de espera reservada.")
else:
    print("O paciente " + nome + " NÃO possui atendimento prioritário e pode aguardar na sala comum!")