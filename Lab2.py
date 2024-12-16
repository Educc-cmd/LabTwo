import math

# Завдання 1: Перевірка порядку чисел A, B, C
def process_variables():
    A = float(input("Введіть значення A: "))
    B = float(input("Введіть значення B: "))
    C = float(input("Введіть значення C: "))
    if A < B < C:
        A *= 2
        B *= 2
        C *= 2
    else:
        A = -A
        B = -B
        C = -C
    print(f"Нові значення: A = {A}, B = {B}, C = {C}")

# Завдання 2: Перевірка точок у коричневій області
def count_points_in_brown_area():
    r = float(input("Введіть радіус кола r: "))
    n_points = int(input("Введіть кількість точок: "))
    points = []
    count = 0
    for i in range(n_points):
        x = float(input(f"Введіть x{i+1}: "))
        y = float(input(f"Введіть y{i+1}: "))
        if x >= 0 and y >= 0 and x**2 + y**2 <= r**2 and y >= x:
            count += 1
    print(f"Кількість точок у коричневій області: {count}")

# Завдання 3: Обчислення суми ряду
def series_sum():
    x = float(input("Введіть значення x: "))
    epsilon = float(input("Введіть ε (точність, наприклад 1e-5): "))
    G = float(input("Введіть G (межа для розбіжності, наприклад 1e3): "))
    n = 1
    series_total = 0.0
    while True:
        u_n = (x**(2*n) + n**x) / math.factorial(n)
        if abs(u_n) < epsilon:
            print("Ряд сходиться.")
            break
        if abs(u_n) > G:
            print("Ряд розходиться.")
            break
        series_total += u_n
        n += 1
    print(f"Сума ряду: {series_total:.10f}")
    print(f"Кількість доданків: {n}")

# Головне меню
while True:
    print("\n*** ГОЛОВНЕ МЕНЮ ***")
    print("1. Завдання 1: Перевірка порядку чисел")
    print("2. Завдання 2: Перевірка точок у коричневій області")
    print("3. Завдання 3: Обчислення суми ряду")
    print("4. Вихід")

    choice = input("Виберіть завдання (1-4): ")

    if choice == '1':
        print("\nВИКОНАННЯ ЗАВДАННЯ 1")
        process_variables()
    elif choice == '2':
        print("\nВИКОНАННЯ ЗАВДАННЯ 2")
        count_points_in_brown_area()
    elif choice == '3':
        print("\nВИКОНАННЯ ЗАВДАННЯ 3")
        series_sum()
    elif choice == '4':
        print("Програма завершена. До побачення!")
        break
    else:
        print("Неправильний вибір. Спробуйте ще раз.")
