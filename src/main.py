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
    newPal = palindrome.replace(' ', '').lower() ## Generate the palindrome to lower case and without the blank spaces.
    BackwardsPalindrome = newPal[::-1] ## Copy the new variable 'newPal' backwards

    if BackwardsPalindrome == newPal: ## If both variables are equals, it´s a palindrome, then return true to continue the first loop 'for' on the function validate().
        print('     The string \'{}\' is a palindrome'.format(palindrome))
        return True
    elif BackwardsPalindrome != newPal: ## If 'BackwardsPalindrome' isn't the same as 'newPal', 'newPal' isn't a palindrome, then return false to continue the second loop 'for' on the function validate().
        print('     The string \'{}\' isn\'t a palindrome'.format(palindrome))
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
