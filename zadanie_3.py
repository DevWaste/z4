A = int(input("Введите начало отрезка A: "))
B = int(input("Введите конец отрезка B: "))

# Гарантируем начало с четного числа
if A % 2 != 0:
    A += 1

even_numbers = ' '.join(str(i) for i in range(A, B + 1, 2))
print("Четные числа на отрезке:", even_numbers)
