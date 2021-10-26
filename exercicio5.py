"5 - Faça um algoritmo para apresentar se dois números são múltiplos."

def multiplo(a,b):
    resto = a % b
    if resto == 0 :
        return "sim"
        
    else:
        return "não"
    
a = int(input())
b = int(input())

print(f'São multiplos :', multiplo(a,b))