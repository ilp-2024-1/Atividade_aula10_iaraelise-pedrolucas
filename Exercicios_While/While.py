#Questão 1
# num = 1

# while num <= 100:
#     print (num)
#     num += 1

# print ("Fim do programa!")

#Questão 2
# valor = 1
# soma = 0

# print("Digite os valores: \n")
# while valor != 0:
#     valor = int(input())
#     soma += valor
# print("A soma dos valores eh", soma,"! \nFim do programa!")

#Questão 3
# senhaSalva = "12345"

# senha = input("Digite sua senha: ")
# while senha != senhaSalva:
#     senha = input("Senha errada! Digite novamente: ")
# print("Senha correta. Fim do programa!")

#Questão 4
# import random

# valorSorteado = random.randint(1, 100)
# print(valorSorteado) 
# #O valor sorteado está impresso apenas para facilitar os testes da questão.

# valor = int(input("Tente adivinhar o valor sorteado e digite um número entre 1 e 100! \n"))
# while valor != valorSorteado:
#     valor = int(input("Valor incorreto! Tente novamente: "))
# print("Parabéns! Você acertou o número sorteado. \nFim do programa!")

#Questão 5
# aux = 1
# fatorial = 1

# num = int(input("Digite um número: "))
# while aux <= num:
#     fatorial = fatorial * aux
#     aux += 1
# print("O número fatorial é: ", fatorial, "\nFim do programa!")

#Questão 6
# anterior = 0
# atual = 1
# termo = 1 #Índicies de posições.

# n = int(input("Digite um número inteiro e positivo: "))
# while termo <= n:
#     if termo == 1:
#         print(anterior)
#     else:
#         print(atual)
#         aux = atual
#         atual += anterior
#         anterior = aux
#     termo += 1
# print("Fim do programa")

#Questão 7
# primo = "é primo."
# n_primo = "não é primo."

# print ("Digite um número de 1 a 10.000")
# num = int(input())

# if num == 3 or num == 2:
#     print (num, primo)
# elif num < 2:
#     print(num, n_primo)
# elif num % 2 == 0 or num % 3 == 0:
#     print(num, n_primo)
# else:
#     print(num, primo)

# print ("Fim do programa!")

#Questão 8
# print ("Digite um número inteiro: ")
# numero = int(input())
# soma = 0

# while numero:
#     digito = numero % 10
#     soma += digito
#     numero = numero // 10

# print ("A soma dos digitos é: ", soma)
# print ("Fim do programa!")

#Questão 9
# soma = 0
# termo = 1 #Índices de psocições.

# n = int(input("Digite um número: "))
# while termo <= n:
#     soma += 1 / termo
#     termo +=1
# print("A soma da séria harmônica é igual a: ", soma, " \nFim do programa!")