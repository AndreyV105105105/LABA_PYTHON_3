def factorial_recursive(user_number):
    if user_number < 0:
        raise ValueError('Число не должно быть меньше 0')

    def fac(n):
        if n == 0:
            return 1
        return n * fac(n - 1)

    answer = fac(user_number)
    return answer