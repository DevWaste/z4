X = int(input("Введите число X: "))
count_divisors = 0

for i in range(1, int(X**0.5) + 1):
    if X % i == 0:
        if i * i == X:
            count_divisors += 1  # Делитель, когда i и X/i совпадают
        else:
            count_divisors += 2  # Добавляем i и X/i

print("Количество делителей числа X:", count_divisors)
