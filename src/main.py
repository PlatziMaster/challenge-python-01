# Resolve the problem!!

PALINDROMES = [
    'Acaso hubo buhos aca',
    'A la catalana banal atacala',
    'Amar da drama',
]
# Here I found a miss " , " between the word "Platzi" and "Oscar"
NOT_PALINDROMES = [
    'Hola como estas',
    'Platzi',
    'Oscar'
]


def is_palindrome(palindrome):
    palindrome = palindrome.replace(' ','').lower()
    new_word = str(palindrome[::-1])
    if new_word == palindrome:
        print('the sentence or word *{}* is a palindrome'.format(new_word))
        return True
    else:
        print('the sentence or word *{}* not is a palindrome'.format(new_word))
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
