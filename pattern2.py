letter_e = [
    ' ##            ##',
    '   ##        ##  ',
    '     ##    ##    ',
    '      ##  ##     ',
    '       ####      ',
    '        ##       ',
    '        ##       ',
]


def draw(repetitions, spacing):
    spaces = ' ' * spacing

    for row_index in range(len(letter_e)):
        for _ in range(repetitions - 1):
            print(letter_e[row_index] + spaces, end='')
        print()


draw(4, 3)