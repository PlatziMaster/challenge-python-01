# Resolve the problem!!
# -*- coding: utf-8 -*-

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


def is_palindrome(palindrome):
    # Start coding here

    # Forma no. 1
    # Utilizando capitalize(), porque en la lista de PALINDROMES cada oración termina con la letra "a"
    # Usando asignación múltiple 

    reversed_palindrome = palindrome[::-1]
    palindrome_capitalize, reversed_palindrome_capitalize = palindrome.capitalize().replace(' ', ''), reversed_palindrome.capitalize().replace(' ', '')
    
    palindrome_result = palindrome_capitalize == reversed_palindrome_capitalize
    return palindrome_result

    # Forma no. 2
    # Usando lower() cambiamos todas las palabras a minúsculas 

    # reversed_palindrome = palindrome[::-1]
    # palindrome_lower_text = palindrome.lower().replace(' ', '')
    # reversed_palindrome_lower_text = reversed_palindrome.lower().replace(' ','')
    # palindrome_result = palindrome_lower_text == reversed_palindrome_lower_text
    # return palindrome_result

def validate():
    for palindrome in PALINDROMES:
        if not is_palindrome(palindrome):
            return False

    for not_palindrome in NOT_PALINDROMES:
        if is_palindrome(not_palindrome):
            return False
    return True


def run():
    if validate():
        print('Completaste el test')
    else:
        print('No completaste el test')


if __name__ == '__main__':
    run()
