# Resolve the problem!!

PALINDROMES = [
    'Acaso hubo buhos aca',
    'A la catalana banal atacala',
    'Amar da drama',
    'Anita lava la tina'
]

NOT_PALINDROMES = [
    'Hola como estas',
    'Platzi'
    'Oscar',
]


def is_palindrome(palindrome):
    # Start coding here
    palindrome = palindrome.replace(' ','').lower()
    return palindrome == palindrome[::-1]


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
