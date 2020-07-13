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
    # Start coding here
    backwards_letters= []
    palindrome_no_spaces = ''
    
    palindrome_no_spaces = ''.join(palindrome.lower().split())

    for letter in palindrome:
        backwards_letters.insert(0, letter.lower())

    backwards_word= ''.join(backwards_letters)
    backwards_word_no_spaces= ''.join(backwards_word.lower().split())

    if backwards_word_no_spaces == palindrome_no_spaces:
        return True
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
