CSI = '\x1b['
RIGHT = f'{CSI}1C'

for i in range(9, 0, -1):
    print(str(i) + RIGHT * (i - 1) + '#')
    f_string = f'{str(i)}{RIGHT * (i - 1)}#'

print('0123456789')