import os

os.system("clear") 

idade = int(input("Digite sua idade: "))

if idade < 16:
    print("Você não pode votar!")
elif 16 <= idade < 17:
    print("O seu voto é opcional!")
elif 18 <= idade <= 65:
    print("O seu voto é obrigatório!")
else:
    print("O seu voto é opcional!")
