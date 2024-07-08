anterior = 0
atual = 1
termo = 1 #Índicies de posições.

n = int(input("Digite um número inteiro e positivo: "))
while termo <= n:
    if termo == 1:
        print(anterior)
    else:
        print(atual)
        aux = atual
        atual += anterior
        anterior = aux
    termo += 1
print("Fim do programa")

