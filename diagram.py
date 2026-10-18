BLOCK = '\u2588'

with open('sequence.txt') as sequence_file:
    file_content = sequence_file.read()

numbers = file_content.split('\n')

# Если нумерация позиций начинается с 1
even_average = sum(
    abs(float(numbers[index]))
    for index in range(len(numbers))
    if (index + 1) % 2 == 0
) / (len(numbers) / 2)

odd_average = sum(
    abs(float(numbers[index]))
    for index in range(len(numbers))
    if (index + 1) % 2 != 0
) / (len(numbers) / 2)

print(even_average, odd_average)

total = even_average + odd_average

even_percent = round(even_average / total * 100, 2)
odd_percent = round(odd_average / total * 100, 2)

print(
    'Чётные:   '
    + str(even_percent)
    + '% : '
    + BLOCK * int(even_percent / 2)
)
print(
    'Нечётные: '
    + str(odd_percent)
    + '% : '
    + BLOCK * int(odd_percent / 2)
)
