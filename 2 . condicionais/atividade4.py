import os

os.system("clear") 

idade = int(input("Digite sua idade: "))

if idade < 18 or idade >= 65: 
    print("O senhor(a) não é obrigado a votar!")
else:
    print("O senhor(a) é obrigado a votar!")


