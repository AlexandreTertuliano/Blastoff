"6 - Uma partida de futebol iniciou na hora A e terminou na hora B. Faça um algoritmo que calcule o tempo que durou a partida."

def tempo(a,b):
    return b -a;
    
a = int(input("Hora inicial:"))
b = int(input("Hora final:"))

print(f'Tempo de partida :', tempo(a,b), 'horas')