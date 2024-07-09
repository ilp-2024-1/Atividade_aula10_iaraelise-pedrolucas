print ("Digite um número inteiro: ")
numero = int(input())
soma = 0

while numero:
    digito = numero % 10
    soma += digito
    numero = numero // 10

print ("A soma dos digitos é: ", soma)
print ("Fim do programa!")