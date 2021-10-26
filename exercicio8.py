"8 - Faça um algoritmo que receba um número e retorne se o número é primo ou não."


n = int(input('Digite o número: '))
contador = 1
contador1 = 0
while contador <= n:
        if n % contador == 0:
            contador1 = contador1+1
            contador = contador+1
        if contador1==2:
            print('O número é primo!')
        else:
            print('O número não é primo!')