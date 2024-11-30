def find_password(n):
    result = ""

    for a in range(1, 20):
        for b in range(a + 1, 21):
            if n % (a + b) == 0:
                result += str(a) + str(b)

    return result

n = int(input("Введите число от 3 до 20: "))
if 3 <= n <= 20:
    password = find_password(n)
    print(f"Пароль для числа {n}: {password}")
else:
    print("Число должно быть в диапазоне от 3 до 20.")
