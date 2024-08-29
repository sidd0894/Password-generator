import random

lowerCaseLetters = 'abcdefghijklmnopqrstuvwxyz'
upperCaseLetters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
nums = '0123456789'
chars = '!@#$$%&_'
stringList = [lowerCaseLetters, upperCaseLetters, nums, chars]
length = ''
numberOfPass = ''


while (type(length) != type(0)):
    try:
        length = (input('Length of password (default is 8): '))
        if (length.strip() == ''):
            length = 8
        elif (int(length) < 4):
            print('Minimum password length should be 4 or greater.')
            length = ''
        else:
            length = int(length)
    except ValueError:
        print('Invalid input.')


while (type(numberOfPass) != type(0)):
    try:
        numberOfPass = (input('Number of passwords to generate (default is 1): '))
        if (numberOfPass.strip() == ''):
            numberOfPass = 1
        else:
            numberOfPass = int(numberOfPass)
    except ValueError:
        print('Invalid input.')


def generatePass():
    password = ''
    for i in range(0, length):
        element = stringList[random.randint(0, len(stringList)-1)]
        password += element[random.randint(0, len(element)-1)]
    return password


for i in range(0, numberOfPass):
    print(generatePass())