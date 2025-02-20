import os

os.system("clear") 

valor_1 = float(input("Digite o primeiro valor: "))
valor_2 = float(input("Digite o segundo valor: "))

media = (valor_1 + valor_2) / 2

print(f"Média: {media}")

soma = (valor_1 + valor_2)

print(f"Soma: {soma}")

produto = (valor_1 * valor_2)

print(f"Produto {produto}")

maior_numero = max(valor_1, valor_2)
menor_numero = min(valor_1, valor_2)

if valor_1 == valor_2:
    print("Eles são iguais")

else:
    print(f"Maior número: {maior_numero}")
    print(f"Menor número: {menor_numero}")



 