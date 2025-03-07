import os 

os.system("clear")

nome = str(input("Digite seu nome: "))
sexo = str(input("Digite seu sexo: ")).lower()

print()

match sexo:
    case "f":
        estado_civil = str(input("Digite o seu estado civil: ")).lower()
        if estado_civil == "casada":
            ano = int(input("Digite quantos anos de casado(a): "))
            print (f"{nome} do sexo {sexo} e {estado_civil} a {ano} anos")
        else:
            print(f"{nome} Estado civil: Solteiro(a).")
    case "m":
        estado_civil = str(input("Digite o seu estado civil: ")).lower()
        if estado_civil == "casado":
            ano = int(input("Digite quantos anos de casado(a): "))
            print (f"{nome} do sexo {sexo} é {estado_civil} a {ano} anos")
        else:
            print(f"{nome} Estado civil: Solteiro(a).")
    case _:
        print("Algo deu errado.")








