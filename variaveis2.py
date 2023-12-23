nome=input("Digite um funcionário: ") #input captura como str
empresa=input("Digite a instituição: ")
qtde_funcionarios=int(input("Digite a quantidade de funcionários: ")) #conversão para int
mediaMensalidade=float(input("Digite a média da mensalidade: ")) #conversão para float
print(nome + " trabalha na empresa " + empresa)
print("Possui: ", qtde_funcionarios, " funcionarios.")
print("A média da mensalidade é de: " + str(mediaMensalidade))
print("==============Verifique os tipos de dados abaixo:==============")
print("O tipo de dado da variavel [nome] é: ",type(nome))
print("O tipo de dado da variavel [empresa] é: ",type(empresa))
print("O tipo de dado da variavel [qtde_funcionarios] é: ",type(qtde_funcionarios))
print("O tipo de dado da variavel [mediaMensalidade] é: ",type(mediaMensalidade))