def bubble_sort(arr):
    # Флаг: были ли обмены на этом проходе
    f = True

    while f:
        f = False
        # Проходим по всем соседним парам
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                # Меняем местами если не по порядку
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                f = True  # Был обмен - продолжаем

        # Если обменов не было - массив отсортирован
        if not f:
            return arr