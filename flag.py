CSI = '\x1b[' # шаблон для команды

YELLOW = f'{CSI}48;5;226m'
GREEN = f'{CSI}48;5;34m'
RED = f'{CSI}48;5;196m'

RESET = f'{CSI}0m'


def draw_line(color, height, width):
    for i in range(height):
        print(f'{color}{" " * width}{RESET}')
        
draw_line(YELLOW, 2, 30)
draw_line(GREEN, 2, 30)
draw_line(RED, 2, 30)
