"10 - Faça um algoritmo que receba um número e retorne o Fatorial desse número"

def fatorial():
    n = int(input("Digite o valor de n: "))
    fat = 1
    i = 2
    while i <= n:
        fat = fat*i
        i = i + 1

    print("O valor de %d! é =" %n, fat)


fatorial()

