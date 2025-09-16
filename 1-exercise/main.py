a = float(input("Введите длину стороны a: "))
b = float(input("Введите длину стороны b: "))
c = float(input("Введите длину стороны c: "))

p = (a + b + c) / 2
square = (p * (p - a) * (p - b) * (p - c)) ** 0.5

print(f"Площадь треугольника: {square:.2f}")