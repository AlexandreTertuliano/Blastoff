"11 - Dada duas lista de números A[1,2,3,4] e B[1,2,5,8], faça um algoritmo que retorne a intersecção das listas"

def intersecao(listA, listB):
    i = list(listA & listB)
    i.sort()

    print(f'A interseção entre as listas A e B é: {i}')


listA = [1,2,3,4]
listB = [1,2,5,8]
a = set(listA)
b = set(listB)
intersecao(a, b)
    