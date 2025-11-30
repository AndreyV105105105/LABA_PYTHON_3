def factorial_recursive(user_number):
    # Проверка на отрицательное число
    if user_number < 0:
        raise ValueError('Число не должно быть меньше 0')

    # Рекурсивная функция для вычисления факториала
    def fac(n):
        if n == 0:
            return 1
        return n * fac(n - 1)

    # Вычисляем и возвращаем результат
    answer = fac(user_number)
    return answer