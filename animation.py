import os
import time

CSI = '\x1b['
HOME = f'{CSI}H'

LETTER_E = [
    ' ##            ##',
    '   ##        ##  ',
    '     ##    ##    ',
    '      ##  ##     ',
    '       ####      ',
    '        ##       ',
    '        ##       ',
]


def draw_letter(position):
    for row in LETTER_E:
        print(' ' * position + row)


while True:
    for position in [0, 5, 10, 15]:
        os.system('cls')
        print(HOME, end='')
        draw_letter(position)
        time.sleep(0.5)