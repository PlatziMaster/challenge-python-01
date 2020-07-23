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
    # Si no es un string, tratamos de convertirlo
    if type(palindrome) != 'string':
        palindrome = str(palindrome)
    # Primero necesito quitar los espacios
    p = palindrome.replace(' ', '')
    # Despues necesito convertir el texto en minúsculas
    p = p.lower()

    # ¿Como podria hacer la comparacion de manera eficiente?
    # Algunas ideas:
    # 1. Partir el string en dos y voltear la segunda mitad y comparar con la primera
    # 2. Algún loop que compare el primer indice con el ultimo y vayan recorriendose
    n = len(p)
    pivot = n // 2  # [1]
    palindrome_found = True
    i = 0

    while palindrome_found and i < pivot:
        print(f'Comparando {p[i]} con {p[n - i - 1]}')
        if (p[i] != p[n - i - 1]):
            # Si encontramos una letra que no es igual, no tiene caso seguir comparando
            palindrome_found = False
        i += 1

    print(f'"{palindrome}" {"es" if palindrome_found else "no es"} un palíndromo')

    return palindrome_found


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
