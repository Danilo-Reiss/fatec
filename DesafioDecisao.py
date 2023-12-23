nivelAcesso=input("Qual o seu nível de acesso?(ADM/USR/GUEST)").upper()
genero=input("Qual o seu gênero? (MASC/FEM)").upper()
#ADM
if nivelAcesso == "ADM":
    if genero == "MASC":
        print("Olá admnistrador!")
    elif genero == "FEM":
        print("Olá admnistradora!")
    else:
        print("Olá desconhecido(a)!")
elif nivelAcesso == "USR":
    if genero == "MASC":
        print("Olá usuário!")
    elif genero == "FEM":
        print("Olá usuária!")
    else:
        print("Olá desconhecido(a)")
elif nivelAcesso == "GUEST":
    if genero == "MASC" or genero == "FEM":
        print("Olá visitante!")
    else:
        print("Olá desconhecido(a)!")
else:
    print("Olá desconhecido(a)!")