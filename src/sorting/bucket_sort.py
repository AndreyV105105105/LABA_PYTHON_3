from src.sorting.quick_sort import quick_sort


def bucket_sort(arr, buckets=None):
    # Если массив пустой - сразу возвращаем
    if not arr:
        return []

    # Преобразуем все элементы в целые числа
    arr = list(map(int, arr))

    # Если количество ведер не указано - вычисляем оптимальное
    if buckets is None:
        buckets = max(1, int(len(arr) ** 0.5))

    # Находим минимальный и максимальный элементы
    mn = min(arr)
    mx = max(arr)

    # Если все элементы одинаковые - возвращаем как есть
    if mn == mx:
        return arr

    # Создаем пустые ведра
    bucket_list = [[] for i in range(buckets)]

    # Распределяем числа по ведрам
    for num in arr:
        # Вычисляем индекс ведра для текущего числа
        index = int((num - mn) / (mx - mn) * (buckets - 1))
        bucket_list[index].append(num)

    # Сортируем каждое ведро быстрой сортировкой
    for i in range(len(bucket_list)):
        bucket_list[i] = quick_sort(bucket_list[i])

    # Собираем все ведра в один отсортированный массив
    result = []
    for bucket in bucket_list:
        result.extend(bucket)

    # Преобразуем обратно в строки и возвращаем
    return list(map(str, result))