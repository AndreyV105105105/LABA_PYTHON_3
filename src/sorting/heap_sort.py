def heap_sort(arr):
    # Преобразуем элементы в целые числа
    arr = list(map(int, arr))

    # Функция для построения кучи
    def kucha(arr, n, i):
        biggest = i  # Корневой элемент
        left = 2 * i + 1  # Левый потомок
        right = 2 * i + 2  # Правый потомок

        # Если левый потомок больше корня
        if left < n and arr[left] > arr[biggest]:
            biggest = left

        # Если правый потомок больше корня
        if right < n and arr[right] > arr[biggest]:
            biggest = right

        # Если наибольший элемент не корень
        if biggest != i:
            # Меняем корень с наибольшим элементом
            arr[i], arr[biggest] = arr[biggest], arr[i]
            # Рекурсивно преобразуем затронутое поддерево
            kucha(arr, n, biggest)

    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        kucha(arr, n, i)

    # Извлечение элементов из кучи
    for i in range(n - 1, 0, -1):
        # Перемещаем текущий корень в конец
        arr[i], arr[0] = arr[0], arr[i]
        # Вызываем функцию кучи на уменьшенной куче
        kucha(arr, i, 0)

    # Преобразуем обратно в строки и возвращаем
    return list(map(str, arr))