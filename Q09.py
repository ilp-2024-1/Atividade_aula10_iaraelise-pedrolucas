soma = 0
termo = 1 #Índices de psocições.

n = int(input("Digite um número: "))
while termo <= n:
    soma += 1 / termo
    termo +=1
print("A soma da séria harmônica é igual a: ", soma, " \nFim do programa!")