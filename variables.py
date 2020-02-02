"""
Картотека автомобилей
"""
# получаем цвет
color = input("Color: ")
# металик текстом
metallic_text = input("Metalic (Yes/Any others): ")
# задаем базовый бит
metallic_bool = False
# приводим текст к биту, если надо
if metallic_text == "Yes":
    metallic_bool = True
# объем двигателя
engine_capacity = float(input("Engine capacity (litre): "))
# пробег
mileage = input("Mileage (km): ")

# выводим типы переменных и значения
print("color", type(color), color)
print("metallic_bool", type(metallic_bool), metallic_bool)
print("engine_capacity", type(engine_capacity), engine_capacity)
print("mileage", type(mileage), mileage)



