Algoritmo "C�lculo m�dia simples"

Var

n1,n2,n3,n4:real
soma, media:real

Inicio
escreva("Digite a nota do 1� bimestre: ")
leia(n1)
escreva("Digite a nota do 2� bimestre: ")
leia(n2)
escreva("Digite a nota do 3� bimestre: ")
leia(n3)
escreva("Digite a nota do 4� bimestre: ")
leia(n4)
soma <- n1+n2+n3+n4
media <- (n1+n2+n3+n4)/4
se (media >= 7) ent�o
escreva("Aprovado!")
senao
escreva("Reprovado!")
fimse

Fimalgoritmo