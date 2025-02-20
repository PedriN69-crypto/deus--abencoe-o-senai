import os

os.system("clear") 

login_cadastrado = "xxx"
senha_cadastrada = "223344"

login = input("Login: ")
senha = input("Senha: ")

if login_cadastrado == login and senha_cadastrada == senha: 
    print("Bem-vindo!")
else:
    print("Login ou senha inválidos!")

