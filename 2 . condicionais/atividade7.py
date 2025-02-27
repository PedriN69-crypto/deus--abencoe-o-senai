import os

os.system("clear") 

produto_1 = float(input("Quantas maçãs o senhor(a) deseja: " ))

if produto_1 < 12:
    preco_maca = 1.30
else:
    preco_maca = 1.00

valor_total = produto_1 * preco_maca

print(f"Valor total R$ {valor_total:.2f}")


