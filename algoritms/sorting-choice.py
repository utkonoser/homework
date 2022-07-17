def find_smallest(arr):
    smallest = arr[0]           # хранит наименьшее значение
    smallest_index = 0          # хранит индекс наименьшего значения
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

print(find_smallest([5, 3, 6, 2, 10]))


def selection_sort(arr):                    # сортирует массив
    new_arr = []                            # создаем новый пустой массив
    for i in range(len(arr)):
        smallest = find_smallest(arr)       # находит наименьший элемент в массиве
        new_arr.append(arr.pop(smallest))   # и добавляет в новый массив
    return new_arr

print(selection_sort([5, 3, 6, 2, 10]))

# В массиве все элементы хранятся в памяти рядом друг с другом
# В списке элементы распределяются в произвольных метсах памяти, при этом
# в одном элементе хранится адрес следующего элемента
# Массивы обеспечивают быстрое чтение
# Списки обеспечивают быструю вставку и выполнение