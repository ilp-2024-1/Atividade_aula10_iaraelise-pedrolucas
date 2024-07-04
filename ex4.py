import random
num = random.randint(1,100)

print ("Digite um valor de 1 a 100: ")
teste = int(input())

while teste != num:
    print ("Continue tentando: ")
    teste = int(input())
    if teste == num:
        print ("Parabéns! Você acertou o número!")