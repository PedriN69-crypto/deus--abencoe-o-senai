import os

os.system("clear")

Valor_produto = float(input("Digite o valor do produto: "))

print("""
=== FORMA DE PAGAMENTO ===
      
1   \tÁ vista
2   \tÁ prazo
      """)

forma_de_pagamento = int(input("Digite a forma de pagamento: "))

match forma_de_pagamento:
    case 1:
         
         desconto = 100 * 0.10
         valor = (Valor_produto - desconto)
         print (f"Valor do produto: R$ {Valor_produto}")
         print (f"Desconto: R$ {desconto}")
         print (f"Total a pagar: R$ {valor}")
         print (f"Forma de pagamento: Á vista")

    case 2:
        parcelas = int(input("Digite em quantas vezes deseja parcelar: "))
        valor = (Valor_produto / parcelas)
        print (f"Valor do produto: R$ {Valor_produto}")
        print (f"Quantidade de parcelas: {parcelas}")
        print (f"Valor por parcela: R$ {valor:.2f}")
        print (f"Forma de pagamento: Á prazo")
        
    case _:
        print ("opção inválida.")
