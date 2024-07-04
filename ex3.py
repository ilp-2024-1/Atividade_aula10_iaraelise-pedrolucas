senha = "abcd"

print ("Digite uma seha de 4 caracteres: ")
teste = input()
while teste != senha:
    print ("Senha incorreta, continue tentando: ")
    teste = input()
    if teste == senha:
        print ("Parabéns, você descobriu a senha!")