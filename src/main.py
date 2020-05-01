# -*- coding: utf-8 -*-

# Resolve the problem!!
"""
PALINDROMES = [
    'Acaso hubo buhos aca',
    'A la catalana banal atacala',
    'Amar da drama',
]

NOT_PALINDROMES = [
    'Hola como estas',
    'Platzi'
    'Oscar',
]
"""

def is_palindrome(palabra):
    # Start coding here
    palindromo = palabra.replace(" ", "")
    palindromo = palindromo.lower()

    inverso = palindromo[::-1]

    if palindromo == inverso:
        return True
    else:
        return False
"""
def validate():
    for palindrome in PALINDROMES:
        if not is_palindrome(palindrome):
            return False

    for not_palindrome in NOT_PALINDROMES:
        if is_palindrome(not_palindrome):
            return False
    return True


def run():
    if is_palindrome():
        print('Completaste el test')
    else:
        print('No completaste el test')
"""

if __name__ == '__main__':

    seguir = 1

    while seguir == 1:

        palabra = str(raw_input('Escribe una palabra: '))

        resultado = is_palindrome(palabra)

        if resultado is True:
            print('{} sí es un palíndromo.'.format(palabra))
        else:
            print('{} no es un palíndromo.'.format(palabra))

        seguir = int(raw_input('Intentar otra vez 1.Si / 2.No : '))
