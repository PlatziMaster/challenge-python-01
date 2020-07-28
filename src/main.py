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

    #First remove the Mayus and Minus
    palindrome = palindrome.casefold()

    #Then i need to remove the spaces in the string
    palindrome = palindrome.replace(" ","")

    #And the string is ready to be reversed
    reverse = palindrome[::-1]

    if reverse == palindrome:
        #print(palindrome, reverse)
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
