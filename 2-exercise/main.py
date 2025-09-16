units = {
    'км': 1000,
    'м': 1,
    'см': 0.01,
    'мм': 0.001,
    'mi': 1609.34,
    'yd': 0.9144
}

print("Поддерживаемые единицы измерения: км, м, см, мм, mi, yd")
source = input("Введите исходную единицу: ").lower()
target = input("Введите целевую единицу: ").lower()
value = float(input("Введите значение: "))

convert = value * units[source]
value = convert / units[target]
print(f"Результат: {value} {target}")