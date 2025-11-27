from src.stack.stack import Stack
def stack_menu():
    print('здесь будет инструкция')
    stack = Stack()
    while True:
        try:
            user_message = input('Введите команду для стэка: ')
            user_message = user_message.lower()
            if  user_message.split()[0] == 'push':
                if len(user_message.split()) == 2:
                    stack.push(user_message.split()[-1])
                else:
                    print('У push должен быть ровно 1 аргумент')

            elif user_message == 'pop':
                print(f'Вы удалили {stack.pop()}')

            elif user_message == 'peek':
                print(stack.peek())

            elif user_message == 'is_empty':
                print(stack.is_empty())

            elif user_message == 'exit':
                break
        except KeyboardInterrupt:
            # Обрабатываем прерывание от клавиатуры (Ctrl+C)
            print('END STACK_PROGRAM')
            return True

        except Exception as err:
            print(err)
            continue
    return True