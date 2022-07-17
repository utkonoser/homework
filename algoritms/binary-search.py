def binary_search(list, item):
    low = 0
    high = len(list) - 1
                                    # границы списка
    while low <= high:               
        mid = (low + high)//2       # середина списка
        guess = list[mid]           # проверяемый элемент списка
        if guess == item:           # если угадали
            return mid
        if guess > item:            # если пров.элем. больше загаданного
            high = mid - 1
        else:                       # если меньше   
            low = mid + 1
    return None                     # если загаданного элемента нет в списке

print(binary_search([1,2,3,4,5,6], 6))