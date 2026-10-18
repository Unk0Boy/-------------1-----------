simvole = '##'


def draw_circles(radius):
    distance = 2 * radius

    for y in range(-radius, radius + 1):
        for x in range(-radius, distance + radius + 1):
            circle1 = (x ** 2 + y ** 2) ** 0.5
            circle2 = ((x - distance) ** 2 + y ** 2) ** 0.5

            if (
                (
                    x >= 0
                    and y <= 0
                    and abs(circle1 - radius) < 0.5
                )
                or (
                    x <= distance
                    and y <= 0
                    and abs(circle2 - radius) < 0.5
                )
            ):
                print(simvole, end='')
            else:
                print('  ', end='')

        print()


draw_circles(10)