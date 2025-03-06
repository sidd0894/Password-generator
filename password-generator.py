import secrets
import string
import argparse
import pyperclip

def main():
    password = ''
    stringList = [string.ascii_lowercase, string.ascii_uppercase, string.digits, '!@#$%&*_']

    parser = argparse.ArgumentParser()
    parser.add_argument('--length', '-len', type=int, default=16, help='length of password', metavar='')
    parser.add_argument('--pass-count', '-count', type=int, default=1, help='number of passwords to generate', metavar='')
    parser.add_argument('--show-pass', '-show', action='store_true', help='use this flag to show password')
    args = parser.parse_args()

    if args.length < 8:
        parser.error('Minimum password length should be 8')
    if args.pass_count < 1:
        parser.error('Pass count should be 1 or greater')

    for i in range(args.pass_count):
        password += ''.join([secrets.choice(secrets.choice(stringList)) for i in range(args.length)])
        password += '\n' if args.pass_count > 1 else ''

    if args.show_pass:
        print(password)

    pyperclip.copy(password)
    print('Password copied !!' if args.pass_count == 1 else 'Copied all passwords !!')


if __name__ == '__main__':
    main()