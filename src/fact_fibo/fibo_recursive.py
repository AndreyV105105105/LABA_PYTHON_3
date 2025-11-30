def fibo_recursive(user_number):
    # Проверка на недопустимое значение
    if user_number <= 0:
        raise ValueError('Число не должно быть меньше 1')

    # Рекурсивная функция для вычисления числа Фибоначчи
    def fib(n):
        if n <= 0:
            return 0
        if n == 1:
            return 1
        return fib(n - 1) + fib(n - 2)

    # Вычисляем и возвращаем результат
    answer = fib(user_number)
    return answer