"2- Dada a distância A e o combustível gasto B, faça um algoritmo para calcular o consumo médio."
def sum(a,b ): 
    return (b/a)

a = int(input('Distancia percorrida: '))
b = int(input('Combustivel gasto: '))


print(f'Foram gastos {sum(a,b)} litros de combustivel por KM ')