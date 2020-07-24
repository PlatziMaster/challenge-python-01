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
    # I will develop this function with loops, it's too easy to do it with slices

    #String preparation: to lowercase and delete the spaces
    palindrome = palindrome.lower()
    palindrome = palindrome.replace(' ', '')

    #loop through each character of the string, comparing the first with the last, and so on.
    str_len = len(palindrome)

    i = 0
    j = str_len - 1

    while i < str_len:
        if palindrome[i] != palindrome[j]:
            return False
        i += 1
        j -= 1

    return True
    
    
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
