"""
Программа для угадывания года рождения А.С. Пушкина (26 мая 1799)
"""
# получаем год от юзера
year = int(input("Which year Pushkin was born? "))

# проверяем год
if year != 1799:
    # выводим, что год неправильный
    print("It is wrong year")
else:
    # получаем день от юзера
    day = int(input("Which day Pushkin was born? "))
    # проверяем день
    if day != 26:
        # выводим, что день неправильный
        print("It is wrong day")
    else:
        # выводим, что хорошо
        print("All rights")
