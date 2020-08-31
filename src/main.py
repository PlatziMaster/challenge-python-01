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
    letter = ''.join(palindrome).replace(' ','').lower() #
    reverse_letter = ''.join(palindrome[::-1]).replace(' ', '').lower()
    if letter == reverse_letter:
        # print('ifpalabra: ', letter)
        # print('ifReversa: ', reverse_letter)
        return True
    else:
        # print('elsepalabra: ', letter)
        # print('elseReversa: ', reverse_letter)
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
