"""
Программа для угадывания года рождения А.С. Пушкина (1799) - вечное
"""
# получаем год от юзера
year = int(input("Which year Pushkin was born?"))

while year != 1799:
    # выводим ошибку, получаем год от юзера еще раз
    year = int(input("You're wrong, try one more time: "))

# выводим что все хорошо
print("You're right")
