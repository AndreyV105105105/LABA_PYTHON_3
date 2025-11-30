def factorial(user_number):
    # Проверка на отрицательное число
    if user_number < 0:
        raise ValueError('Число не должно быть меньше 0')

    # Внутренняя функция для вычисления факториала
    def fac(n):
        ans = 1
        # Умножаем все числа от 1 до n
        for i in range(1, n + 1):
            ans *= i
        return ans

    # Вычисляем и возвращаем результат
    answer = fac(user_number)
    return answer