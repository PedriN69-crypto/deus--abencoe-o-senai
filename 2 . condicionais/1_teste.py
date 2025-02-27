import os

os.system("clear")
          
salario = float(input("Informe o seu sálario: "))

if salario <= 3000:
    print("Cargo De: Programador Junior")
elif salario > 3000 and salario <= 6000:
    print("Cargo De: Programador Pleno")
elif salario > 6000 and salario <= 15000:
    print("Cargo De: Programador Senior")
else:
    print("Cargo De: Gerente de Projetos")

print()

listas_numeros = [1, 2, 3]

listas_numeros[0] = 5
 
print(listas_numeros[1])
print(listas_numeros[2])
print(listas_numeros[3])

print()

for x in range (5):
    print (x) == 0
    print (x) == 1
    print (x) == 3
    print (x) == 4
