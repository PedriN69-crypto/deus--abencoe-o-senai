import os

os.system("clear") 

valor_1 = float(input("Digite o primeiro valor: "))
valor_2 = float(input("Digite o segundo valor: "))
valor_3 = float(input("Digite o terceiro valor: "))

print(f"Primeiro número: {valor_1}")
print(f"Segundo número: {valor_2}")
print(f"Terceiro número: {valor_3}")

maior_numero = max(valor_1, valor_2, valor_3)
menor_numero = min(valor_1, valor_2, valor_3)

print(f"Maior número: {maior_numero}")
print(f"Menor número: {menor_numero}")