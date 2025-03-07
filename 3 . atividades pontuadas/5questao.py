import os

os.system("clear")

primeiro_numero = float(input("Digite o primeiro número: "))
operacao = input("Digite a operação desejada: ")
segundo_numero = float(input("Digite o segundo número: "))

match operacao:
    case "+":
        resultado = primeiro_numero + segundo_numero
    case "-":
        resultado = primeiro_numero - segundo_numero
    case "/": 
        resultado = primeiro_numero / segundo_numero
    case "*":
        resultado = primeiro_numero * segundo_numero
    case _:
        resultado = "Operação inválida."

print()
print(f"Primeiro número: {primeiro_numero}") 
print(f"Operação: {operacao}")
print(f"Segundo número: {segundo_numero}") 
print(f"Resultado: {resultado}") 