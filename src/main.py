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
    simpleword= []
    reverseword= []
    for char in palindrome:
        if char != ' ':
            simpleword.append(char.lower())
    print(simpleword)
    for char in reversed(simpleword):
        reverseword.append(char)
    print(reverseword)

    if simpleword == reverseword:
        return True
    else:
        return False
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
