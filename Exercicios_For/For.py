#Questão 1 
# for i in range (2, 13, 2):
#     print (i, end=",")
# print ('...')

#Questão 2
# numero = int(input("Digite um número: "))
# for i in range (1, numero + 1):
#     print (i, end=",") 
# print ("Fim.")

#Questão 3
# v_ini = int(input("Insira um valor positivo: "))
# v_fim = int(input("Insira um segundo valor positivo: "))

# for i in range (v_ini, v_fim+1):
#     print (i, end=(","))
# print ("\n Fim do programa!")

#Questão 4 
# v_ini = int(input("Insira um valor positivo: "))
# v_fim = int(input("Insira outro valor positivo: "))

# for i in range (v_ini+1, v_fim):
#     print (i, end=(","))
# print ("\n Fim do programa!")

#Questão 5
soma = 0
v_ini = int(input("Insira um valor positivo: "))
v_fim = int(input("Insira outro valor positivo: "))

for i in range (v_ini, v_fim+1):
    # numero = i
    # divisores = 0
    # print (i, end=(","))

    # for i in range (1, numero+1):
    #     if (numero % i) == 0:
    #         divisores += 1

    #     if divisores == 2:
    #         print (f"{numero}")
    #         soma_primo += numero
    if (i != 1):
        if (i == 5):
            print (i, end=",")
            soma = soma + i
        if (i % 5 != 0):
            if (i == 2):
                print (i, end=",")
                soma = soma + i
            elif (i == 3):
                print (i, end=",")
                soma = soma + i
            elif (i % 2 != 0 and i% 3!=0):
                print (i, end=",")
                soma = soma + i

print ("\n Somatória dos números primos: ", soma)
print ("\n Fim do programa!")