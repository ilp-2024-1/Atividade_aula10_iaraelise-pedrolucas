import random

valorSorteado = random.randint(1, 100)
print(valorSorteado) 
#O valor sorteado está impresso apenas para facilitar os testes da questão.

valor = int(input("Tente adivinhar o valor sorteado e digite um número entre 1 e 100! \n"))
while valor != valorSorteado:
    valor = int(input("Valor incorreto! Tente novamente: "))
print("Parabéns! Você acertou o número sorteado.")