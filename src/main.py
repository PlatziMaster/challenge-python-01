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
    without_blanks = []
    cut_word = []

    for letter in palindrome:
        if letter != ' ':
            cut_word.insert(0, letter)
        without_blanks = without_blanks + cut_word
        cut_word = []
    full_sentence = ''.join(without_blanks)
    full_sentence = full_sentence.lower()
    reversed_word = full_sentence[::-1]
    print(full_sentence)
    print(reversed_word)
    if reversed_word == full_sentence:
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
