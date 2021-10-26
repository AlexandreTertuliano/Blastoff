"13 - Faça um algoritmo que receba uma matriz[i,z] como parâmetro e imprima todos os valores dessa matriz."


import random
def matriz(n_linhas, n_colunas):
    matriz = [] 
    linha = []
    i = 0

    while len(matriz) != n_linhas:
        n = i
        i= i+1
        linha.append(n)
       

        if len(linha) == n_colunas:
           
            matriz.append(linha)
            linha = []
            
    return matriz 
    
a = int(input("Digite o numero de linhas:"))
b = int(input("Digite o numero de colunas:"))


print(matriz(a,b))