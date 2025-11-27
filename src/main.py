
from src.additional_functions.run import run


def main():
    """
    Главная функция приложения.
    Запускает основной цикл программы.
    """
    print('Здесь будет инструкция')
    try:
        # Запускаем основной цикл программы
        run()
    except Exception as err:
        return False


if __name__ == "__main__":
    main()