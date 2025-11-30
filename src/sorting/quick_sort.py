def quick_sort(arr):
    arr = list(map(int, arr))
    # Массивы из 0 или 1 элемента уже отсортированы
    if len(arr) <= 1:
        return list(map(str, arr))

    # Выбираем опорный элемент - средний элемент массива
    support_el = arr[len(arr) // 2]

    # Разделяем массив на три части:
    # - элементы меньше опорного
    left = [el for el in arr if el < support_el]
    # - элементы равные опорному
    middle = [x for x in arr if x == support_el]
    # - элементы больше опорного
    right = [x for x in arr if x > support_el]

    # Рекурсивно сортируем левую и правую части, объединяем с серединой
    return list(map(str, quick_sort(left) + middle + quick_sort(right)))