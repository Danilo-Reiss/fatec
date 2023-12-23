Algoritmo "Cálculo média simples"

Var

n1,n2,n3,n4:real
soma, media:real

Inicio
escreva("Digite a nota do 1º bimestre: ")
leia(n1)
escreva("Digite a nota do 2º bimestre: ")
leia(n2)
escreva("Digite a nota do 3º bimestre: ")
leia(n3)
escreva("Digite a nota do 4º bimestre: ")
leia(n4)
soma <- n1+n2+n3+n4
media <- (n1+n2+n3+n4)/4
se (media >= 7) então
escreva("Aprovado!")
senao
escreva("Reprovado!")
fimse

Fimalgoritmo