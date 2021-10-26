"1- Dada as idades I, J, K, X, Y. Faça um algoritmo para calcular a média das idades."

def sum(i, j, k , l, x ,y ): 
    return ((i + j + k + l + x + y) / 6)

i = int(input('Enter 1st age: '))
j = int(input('Enter 2nd age: '))
k = int(input('Enter 3nd age: '))
l = int(input('Enter 4nd age: '))
x = int(input('Enter 5nd age: '))
y = int(input('Enter 6nd age: '))

print(f'Average of {i} and {j} and {k} and {l} and {x} and {y} is {sum(i, j, k , l, x ,y )}')