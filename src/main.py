# Resolve the problem!!

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
    # Si no es un string, tratamos de convertirlo
    type(palindrome) != 'string':
        palindrome = str(palindrome)
    # Primero necesito quitar los espacios
    palindrome = palindrome.replace(' ', '')
    # Despues necesito convertir el texto en minúsculas
    palindrome = palindrome.lower()
    # ¿Como podria hacer la comparacion de manera eficiente?
    # Algunas ideas
    # - Partir el string en dos y voltear la segunda mitad y comparar con la primera
    # - Algun loop que compare el primer indice con el ultimo y vayan recorriendose
    # Start coding here
    pass


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
