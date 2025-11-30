from src.fact_fibo.factorial import factorial
from src.fact_fibo.factorial_recursive import factorial_recursive
from src.fact_fibo.fibo import fibo
from src.fact_fibo.fibo_recursive import fibo_recursive

from src.sorting.bubble_sort import bubble_sort
from src.sorting.quick_sort import quick_sort
from src.sorting.counting_sort import counting_sort
from src.sorting.radix_sort import radix_sort
from src.sorting.bucket_sort import bucket_sort
from src.sorting.heap_sort import heap_sort

from src.stack.stack_menu import stack_menu


def run():
    """
    Основной цикл программы.
    Обрабатывает пользовательские команды и вызывает соответствующие функции.
    """
    while True:
        try:
            # Получаем команду от пользователя
            user_message = input('Введите команду: ')
            user_message = user_message.lower()

            # Словари с доступными функциями
            func_dict1 = {'1': factorial, '2': factorial_recursive, '3': fibo, '4': fibo_recursive}
            func_dict2 = {'5': bubble_sort, '6': quick_sort, '7': counting_sort, '8': radix_sort, '9': bucket_sort,
                          '10': heap_sort}

            # Обработка команд для функций факториала и Фибоначчи
            if user_message in func_dict1:
                user_number = int(input('Введите число: '))
                answer = func_dict1[user_message](user_number)
                print(answer)

            # Обработка команд для функций сортировки
            if user_message in func_dict2:
                user_list = (input('Введите числа через пробел: ')).split()
                answer = func_dict2[user_message](user_list)
                print(' '.join(answer))

            # Обработка команды для работы со стеком
            elif user_message == '11':
                stack_menu()

            # Выход из программы
            elif user_message == 'exit':
                break

        except KeyboardInterrupt:
            # Обрабатываем прерывание от клавиатуры (Ctrl+C)
            print('END PROGRAM')
            return True

        except Exception as err:
            # Обрабатываем все остальные ошибки
            print(f"Произошла ошибка: {err}")
            continue

    return True