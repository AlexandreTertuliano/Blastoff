"7 - Dada uma lista de números A[1,2,3,…], faça um algoritmo que retorne uma lista somente com os números pares."

list = []

n = int(input("Numeros de elementos na lista : "))

for i in range(0, n):
    num = int(input())
    
    if num % 2  == 0:
        list.append(num)
    
    

print(list)