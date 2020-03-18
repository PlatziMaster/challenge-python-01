# Resolve the problem!!

PALINDROMES = [
    'Acaso hubo buhos aca',
    'A la catalana banal atacala',
    'Amar da drama',
    "Mr. Owl ate my metal worm",
    "Do geese see God?",
    "Was it a car or a cat I saw?",
    "Murder for a jar of red rum",
    "Go hang a salami, I'm a lasagna hog",
    "Rats live on no evil star",
    "Live on time, emit no evil",
    "Step on no pets",
    'bob',
    'rayar',
    'Anita lava la tina',
    'sometemos',
    'ojo'
]

NOT_PALINDROMES = [
    'Hola como estas',
    'Platzi'
    'Oscar',
]


def is_palindrome(palindrome):
    word = palindrome.replace(" ","").replace(".","").replace("'","").replace("?","").lower().replace("á","a").replace("é","e").replace("í","i").replace("ó","o").replace("ú","u")
    reversed_word = word[::-1]

    if reversed_word == word:
        return True
    else:
        print(palindrome)
        return False
    pass

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
