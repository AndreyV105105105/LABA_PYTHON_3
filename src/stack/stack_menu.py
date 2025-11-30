from src.stack.stack import Stack


def stack_menu():
    """
    Меню для работы со стеком.
    Обрабатывает команды пользователя для операций со стеком.
    """
    print("\nМЕНЮ СТЕКА")
    print("push <значение> - Добавить элемент в стек")
    print("pop - Удалить и вернуть верхний элемент")
    print("peek - Показать верхний элемент без удаления")
    print("is_empty - Проверить пуст ли стек")
    print("exit - Вернуться в главное меню")

    # Создаем экземпляр стека
    stack = Stack()

    while True:
        try:
            # Получаем команду от пользователя
            user_message = input('Введите команду для стэка: ')
            user_message = user_message.lower()

            # Обработка команды push (добавление элемента)
            if user_message.split()[0] == 'push':
                if len(user_message.split()) == 2:
                    # Добавляем элемент в стек
                    stack.push(user_message.split()[-1])
                else:
                    print('У push должен быть ровно 1 аргумент')

            # Обработка команды pop (удаление и возврат верхнего элемента)
            elif user_message == 'pop':
                print(f'Вы удалили {stack.pop()}')

            # Обработка команды peek (просмотр верхнего элемента без удаления)
            elif user_message == 'peek':
                print(stack.peek())

            # Обработка команды is_empty (проверка пустоты стека)
            elif user_message == 'is_empty':
                print(stack.is_empty())

            # Выход из меню стека
            elif user_message == 'exit':
                break

        except KeyboardInterrupt:
            # Обрабатываем прерывание от клавиатуры (Ctrl+C)
            print('END STACK_PROGRAM')
            return True

        except Exception as err:
            # Обрабатываем все остальные ошибки
            print(f"Произошла ошибка в меню стека: {err}")
            continue

    return True