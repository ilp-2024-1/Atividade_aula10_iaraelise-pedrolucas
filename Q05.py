aux = 1
fatorial = 1

num = int(input("Digite um número: "))
while aux <= num:
    fatorial = fatorial * aux
    aux += 1
print("O número fatorial é: ", fatorial)
