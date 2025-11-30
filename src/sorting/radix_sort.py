def radix_sort(arr, base=10):
    # Если пустой массив, возвращаем пустой
    if len(arr) == 0:
        return []

    # Преобразуем элементы в целые числа
    arr = list(map(int, arr))

    # Определяем максимальное количество разрядов
    max_range = len(str(max(arr)))

    # Создаем корзины для каждой цифры
    buckets = [[] for i in range(base)]

    # Проходим по всем разрядам
    for i in range(0, max_range):
        # Распределяем числа по корзинам по текущей цифре
        for el in arr:
            digit = (el // base ** i) % base
            buckets[digit].append(el)

        # Собираем числа обратно в массив
        arr = []
        for bucket in buckets:
            for el in bucket:
                arr.append(str(el))

        # Очищаем корзины для следующего разряда
        buckets = [[] for i in range(base)]

    return arr