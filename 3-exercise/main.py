year = int(input("Введите год: "))

if year % 4 == 0 or year % 400 == 0:
    print(f"{year} - високосный")
elif year % 100 == 0:
    print(f"{year} - не високосный")
else:
    print(f"{year} - не високосный")