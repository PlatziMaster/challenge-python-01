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
    # Start coding here

    # USING PYTHON METHODS
    # palin = palindrome.replace(' ', '').lower()
    # return palin == palin[::-1]

    # WITHOUT PYTHON METHODS
    palin = ''
    for char in palindrome:
        if char != ' ':
            palin += char
    
    cont = len(palin)-1
    reverse = ''
    while(cont >= 0):
        reverse += palin[cont]
        cont -= 1

    return palin.lower() == reverse.lower()

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
