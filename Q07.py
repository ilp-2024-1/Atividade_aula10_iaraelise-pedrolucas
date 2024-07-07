primo = "é primo."
n_primo = "não é primo."

print ("Digite um número de 1 a 10.000")
num = int(input())

if num == 3 or num == 2:
    print (num, primo)
elif num < 2:
    print(num, n_primo)
elif num % 2 == 0 or num % 3 == 0:
    print(num, n_primo)
else:
    print(num, primo)

print ("Fim do programa!")