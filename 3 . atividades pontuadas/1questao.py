import os 

os.system("clear")

opcao_a = float(input("Digite o valor A: "))
opcao_b = float(input("Digite o valor B: "))
opcao_c = float(input("Digite o valor C: "))

soma = (opcao_a + opcao_b)

print()

print (f"Soma dos algarismos A e B: {soma}")

print()

if soma < opcao_c:
    print("A + B é menor que C")
else:
    print("A + B é maior que C")


