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
    # Comencemos convirtiendo a lower case el palindrome
    palindrome = palindrome.lower()
    # se parte el palindromo en tokens
    palindrome = palindrome.split(' ')
    #se usen los tokens
    palindrome=''.join(palindrome)
    # construyamos un reverse del palindrome
    palindrome_reverse = palindrome[::-1]
    # finalmente comparemos si palindrome_lower y reverse son iguales
    if palindrome==palindrome_reverse:
        return True
    else:
        return False
    

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
