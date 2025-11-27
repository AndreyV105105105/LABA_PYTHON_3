


def factorial(user_number):
    if user_number < 0:
        raise ValueError('Число не должно быть меньше 0')

    def fac(n):
        ans = 1
        for i in range(1, n + 1):
            ans *= i
        return ans

    answer = fac(user_number)
    return answer
