from src.fact_fibo.factorial import factorial
from src.fact_fibo.factorial_recursive import factorial_recursive
from src.fact_fibo.fibo import fibo
from src.fact_fibo.fibo_recursive import fibo_recursive


def run():
        while True:
            try:
                user_message = input('Введите команду: ')
                user_message = user_message.lower()
                func_dict = {'1': factorial, '2': factorial_recursive, '3': fibo, '4': fibo_recursive}
                if user_message in func_dict:
                    user_number = int(input('Введите число: '))
                    answer = func_dict[user_message](user_number)
                    print(answer)

                elif user_message == 'exit':
                    break
            except KeyboardInterrupt:
                # Обрабатываем прерывание от клавиатуры (Ctrl+C)
                print('END PROGRAM')
                return True

            except Exception as err:
                print(err)
                continue
        return True
