import os

os.system("clear")

print("""
 =========Calendario=========
 Código \tDia da semana 
 1      \tJaneiro 
 2      \tFevereiro
 3      \tMarço
 4      \tAbril
 5      \tMaio
 6      \tJunho
 7      \tJulho
 8      \tAgosto
 9      \tSetembro
 10     \tOutubro
 11     \tNovembro
 12     \tDezembro
 """)

opcao = int(input("digite o codgio correspondente aos meses do ano : "))

match opcao :
    case 1 :

     resultado = "Janeiro" 
        
    case 2 :
      
     resultado = "Fevereiro" 
        
    case 3 :
    
     resultado = "Março"  
        
    case 4 :
    
     resultado = "Abril" 
        
    case 5 :
    
     resultado = "Maio" 
        
    case 6 :
    
     resultado = "Junho" 
        
    case 7 :

        resultado = "Julho" 
        
    case 8 :
    
     resultado = "Agosto" 
        
    case 9 :

        resultado = "Setembro" 
        
    case 10 :

        resultado = "Outubro" 
       
    case 11 :

        resultado = "Novembro" 
        
    case 12 :

        resultado = "Dezembro" 
        
    
print()
print(f"Mês do ano: {resultado}")
