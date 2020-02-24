# Resolve the problem!!

PALINDROMES = [
    'Acaso hubo buhos aca',
    'A la catalana banal atacala',
    'Amar da drama',
]

NOT_PALINDROMES = [
    'Hola como estas',
    'Platzi',
    'Oscar',
]


def is_palindrome(palindrome):
    palindrome = palindrome.replace(" ","").lower()
    reverse = ''.join(reversed(palindrome))
    #print (palindrome)
    #print (nospaces)
    if reverse == palindrome:
        print (palindrome, 'is palindrome :)')
        return True
    else:
        print (palindrome, 'is not palindrome :(')        
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
