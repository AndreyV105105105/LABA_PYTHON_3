def counting_sort(arr):
    # Пустой массив - возвращаем пустой
    if len(arr) == 0:
        return []

    # Преобразуем элементы в целые числа
    arr = list(map(int, arr))

    # Находим диапазон значений
    mx = max(arr)
    mn = min(arr)

    # Создаем массив для подсчета (диапазон от mn до mx)
    count = [0] * (mx - mn + 1)

    # Считаем количество каждого элемента
    for el in arr:
        count[el - mn] += 1

    # Восстанавливаем отсортированный массив
    result = []
    for i in range(len(count)):
        # Добавляем элемент (i + mn) count[i] раз
        result.extend([str(i + mn)] * count[i])

    return result