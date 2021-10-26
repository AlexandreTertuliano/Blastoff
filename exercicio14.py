"14 - Faça um algoritmo que recebe uma palavra e retorne se a palavra é palíndromo. (Palavra que se pode ler, indiferentemente, da esquerda para direita ou vice-versa. Ex: osso, Ana e etc)."

def palindromo(palavra):
    if palavra == palavra[::-1]:
        return True
    return False


palavra = input('Digite uma palavra: ').lower().strip().replace(' ', '')

print(palindromo(palavra))