"""
Программа для угадывания года рождения:
А.С. Пушкина (1799)
Л.Н. Толстой (1828)
Ф.М. Достоевский (1821)
А.С. Есенин (1895)
А.С. Ахматова (1889)
"""
#   переменная для выхода продолжения игры
is_continue = "Yes"
#   переменная для суммы правильных
rating = 0
#   зацикливаем игру
while is_continue == "Yes":

    # получаем 1ый год от юзера
    year = int(input("Which year Pushkin was born? "))

    if year == 1799:
        rating += 1

    # получаем 2ый год от юзера
    year = int(input("Which year Lev Tolstoy was born? "))

    if year == 1828:
        rating += 1

    # получаем 3ый год от юзера
    year = int(input("Which year Dostoevsky was born? "))

    if year == 1821:
        rating += 1

    # получаем 4ый год от юзера
    year = int(input("Which year Esenin was born? "))

    if year == 1895:
        rating += 1

    # получаем 5ый год от юзера
    year = int(input("Which year Akhmatova was born? "))

    if year == 1889:
        rating += 1

    #   выводим результаты
    print("Right answers:", rating)
    print("Wrong answers:", 5 - rating)
    print("Rate:", rating * 20)

    #   обнулем рейтинг
    rating = 0

    #   спрашиваем, хотят ли продолжить
    is_continue = input("Do you want to try one more time (Yes/anu others): ")
