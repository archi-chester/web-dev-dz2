"""
Программа для угадывания года рождения А.С. Пушкина (1799)
"""
# получаем год от юзера
year = int(input("Which year Pushkin was born?"))

if year != 1799:
    print("You're wrong")
else:
    print("You're right")
