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
    """
    validates that the string palindrome is a 
    palindrome (it is a word or phrase that 
    read equal to right and back

    param str palindrome is a word or Phrase

    returns True if the word or phrase is a  
    palindorme or False if not.
    """
    
    reversed_letters = palindrome[::-1]

    if reversed_letters.lower().replace(' ','') == palindrome.lower().replace(' ',''):
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
