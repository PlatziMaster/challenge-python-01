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
    # Limpiamos el string, eliminamos espacios y pasamos a minúsculas
    word = palindrome.replace(" ","")
    word = word.lower()
    # Obtenemos el tamaño del string para iterar únicamente la mitad del string
    size = len(word)
    size = int(size/2 + 1)
    for n in range(0, size):
        if word[n] != word[-1-n]:
            break
    else:
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
