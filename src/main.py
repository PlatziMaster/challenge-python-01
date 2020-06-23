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
    myList = []
    counter = -1
    letra = ""
    newList = []
    for len in palindrome:
        if len == "A":
            myList.append("a")
            counter += 1
        elif len == "H":
            myList.append("h")
            counter += 1
        elif len == "P":
            myList.append("p")
            counter += 1
        elif len == "O":
            myList.append("o")
            counter += 1
        elif len != " ":
            myList.append(len)
            counter += 1
    while counter >= 0:
        newList.append(myList[counter])
        counter -= 1
    if myList == newList:
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
