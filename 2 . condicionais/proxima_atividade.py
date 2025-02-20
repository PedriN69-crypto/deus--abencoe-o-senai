import os

os.system("clear") 

nota_1 = int(input("Digite sua primeira nota: "))
nota_2 = int(input("Digite sua segunda nota: "))
nota_3 = int(input("Digite sua terceira nota: "))

media = (nota_1 + nota_2 + nota_3) / 3

if media == 7:
    print("Aprovado!")
if media < 7:
    print("Reprovado!")

print(f"Média: {media}")

