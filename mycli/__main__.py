import os

from clearterminal import clear, system

from saves import *
from consts import *

clear()
print(f'MyCLI has been launched.\nEnter help to see the list of commands.\n\n')

def nextf():
    if save['autoclear']:
        input('\nPress Enter to continue')
        clear()
    else:
        print()

while True:
    uinput = input(os.save['inputstyle']).split()

    args = None
    if len(uinput) > 1:
        args = uinput[1:]
    elif len(uinput) == 0:
        nextf()
        continue

    command = uinput[0]

    if len(uinput) > 1:
        args = uinput[1:]

    if command == 'help':
        print(COMMANDS)

    elif command == 'clear':
        clear()

    elif command == 'inputstyle':
        if args is not None:
            save['inputstyle'] = ' '.join(args) + ' '
            savef()
        else:
            print('Invalid syntax! Correct - inputstyle [style]')
    
    elif command == 'autoclear':
        if args is not None:
            if args[0] in STRBOOL:
                save['autoclear'] = STRBOOL[args[0]]
                savef()
                nextf()
                continue
        print('Invalid syntax! Correct - autoclear [0/1]')
    
    elif command == 'open':
        if args is not None:
            if system == 'Windows':
                os.system(f'start {args[0]}')
            else:
                os.system(f'xdg-open {args[0]}')
        else:
            print('Invalid syntax! Correct - open [path]')

    elif command == 'exit':
        break

    else:
        print('Unknown command! Enter help to see the list of commands.')

    nextf()

print('Goodbye!\n')
