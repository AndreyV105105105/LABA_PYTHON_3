
def fibo_recursive(user_number):
    if user_number <= 0:
        raise ValueError('Число не должно быть меньше 1')

    def fib(n):
        if n <= 0:
            return 0
        if n == 1:
            return 1
        return fib(n - 1) + fib(n - 2)

    answer = fib(user_number)
    return answer