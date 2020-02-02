"""
Программа для угадывания года рождения А.С. Пушкина (26 мая 1799) - вечная
"""
# получаем год от юзера
year = int(input("Which year Pushkin was born? "))

# проверяем год
while year != 1799:
    # выводим, что год неправильный
    year = int(input("It is wrong year, try on more time: "))

# получаем день от юзера
day = int(input("Which day Pushkin was born? "))

# проверяем день
while day != 26:
    #    выводим, что день неправильный
    day = int(input("It is wrong day, try on more time: "))

# выводим, что хорошо
print("All rights")
