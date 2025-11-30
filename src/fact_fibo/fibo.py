def fibo(user_number):
    # Проверка на недопустимое значение
    if user_number <= 0:
        raise ValueError('Число не должно быть меньше 1')

    # Функция для вычисления числа Фибоначчи
    def fib(n):
        if n == 1:
            return 1
        a, b = 0, 1
        for i in range(2, n + 1):
            a, b = b, a + b
        return b

    # Вычисляем и возвращаем результат
    answer = fib(user_number)
    return answer