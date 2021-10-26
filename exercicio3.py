"3 - Dados três números (a, b, c), faça um algoritmo para mostrar o menor número."

def menor(a,b,c):
    min = a

    if b < min:
        min = b
    if c < min:
        min = c

    return min

a = int(input('Primeiro numero: '))
b = int(input('Segundo numero: '))
c = int(input('Terceiro numero: '))


print("Menor numero é : ", menor(a,b,c))