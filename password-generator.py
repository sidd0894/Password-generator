import random
import pyperclip

lowerCaseLetters = 'abcdefghijklmnopqrstuvwxyz'
upperCaseLetters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
nums = '0123456789'
chars = '!@#$$%&_'
stringList = [lowerCaseLetters, upperCaseLetters, nums, chars]
length = ''
numberOfPass = ''
passwordList = []


def getUserInput(prompt: str, default, min):
    while True:
        try:
            num = input(prompt).strip()
            if num == '':
                num = default
                break

            elif int(num) < min:
                print(f'Minimum value can be {min}')

            else:
                num = int(num)
                break

        except ValueError:
            print('Invalid input.')

    return num




def generatePass(length):
    password = ''
    for i in range(0, length):
        element = stringList[random.randint(0, len(stringList)-1)]
        password += element[random.randint(0, len(element)-1)]
    return password




def main():
    print('\n(NOTE - Leave empty to use default values.)')

    length = getUserInput('Length of password (default is 8): ', 8, 4)
    numberOfPass = getUserInput('Number of passwords to generate (default is 1): ', 1, 1)
    
    for i in range(0, numberOfPass):
        password = generatePass(length)
        passwordList.append(password)
        print(f'{i+1}.  {password}')


    if len(passwordList) > 0:
        while True:
            try:
                passwordIndex = int(input(f'Enter serial number of password to copy: ').strip())
                passwordIndex = passwordIndex - 1

                if passwordIndex >= 0 and passwordIndex < len(passwordList):
                    try:
                        pyperclip.copy(passwordList[passwordIndex]) 
                        print('Copied !!')

                    except Exception as e:
                        print(f'[ERROR]: {e}')

                    break

                else:
                    print(f'[ERROR] No password present at serial number {passwordIndex + 1}')

            except KeyboardInterrupt:
                print('\nKeyboard interruption. Exiting...')
                break
            except:
                print('[ERROR] Invalid input')




if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\nKeyboard interruption. Exiting...')