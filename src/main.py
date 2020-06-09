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
    palindrome = palindrome.lower()
    Fifo = []
    Lifo = []
    Slot = 0
    PalindromeSize = len(palindrome)

    for Slot in range(0, PalindromeSize):
        SlotCheck = palindrome[Slot]
        if SlotCheck != " ":
            Fifo.append(SlotCheck)

    LifoHelp = reversed(Fifo)
    Error = 0
    Slot = 0

    for eachSlot in LifoHelp:
        Lifo.append(eachSlot)
        if Lifo[Slot] != Fifo[Slot]:
            Error = 1
            break
        Slot += 1

    if Error == 1:
        return False
    else:
        return True

def validate():
    for palindrome in PALINDROMES:
        if not is_palindrome(palindrome):
            return False

    for not_palindrome in NOT_PALINDROMES:
        if is_palindrome(not_palindrome):
            return False
    return True
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
