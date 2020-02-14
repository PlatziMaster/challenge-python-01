# Resolve the problem!!
import string

SYMBOLS = list('!"#$%&\'()*+,-./:;?@[]^_`{|}~')


def generate_password():
    # Start coding here


def validate(password):

    has_lowercase_letters = False
    has_numbers = False
    has_uppercase_letters = False
    has_symbols = False

    for char in password:
        if char in string.ascii_lowercase:
            has_lowercase_letters = True
            break

    for char in password:
        if char in string.ascii_uppercase:
            has_uppercase_letters = True
            break

    for char in password:
        if char in string.digits:
            has_numbers = True
            break

    for char in password:
        if char in SYMBOLS:
            has_symbols = True
            break

    if has_symbols and has_numbers and has_lowercase_letters and has_uppercase_letters:
        return True
    return False


def run():
    password = generate_password()
    if validate(password):
        print('Secure Password')
    else:
        print('Insecure Password')


if __name__ == '__main__':
    run()
