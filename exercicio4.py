"4 - Faça um algoritmo que converta a temperatura de C para F. Utilize a fórmula"

def conversor(c):
    return ((c * 1.8) + 32)

c = float(input('Temperatura em Celsius: '))



print("Temperatura em Farenheit : ", conversor(c))