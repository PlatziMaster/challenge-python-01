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
    reverse_palindrome = palindrome[-1::-1]
    text_lower_whitout_space = palindrome.lower().replace(' ', '')
    reverse_text_lower_whitout_space = reverse_palindrome.lower().replace(' ', '')
    palindrome_value = (text_lower_whitout_space ==
                        reverse_text_lower_whitout_space)

    return palindrome_value


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
