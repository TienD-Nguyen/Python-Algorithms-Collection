"""
Quick Sort Algorithm

*   22/01/2022  Initial code
*   23/01/2022  Added quick_sort and partition methods separately

"""

def quick_sort_first(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    i = 0

    for j in range(1, len(arr)):
        if arr[j] <= pivot:
            arr[j], arr[i+1] = arr[i+1], arr[j]
            i += 1

    arr[i], arr[0] = arr[0], arr[i]

    left = quick_sort_first(arr[:i])
    right = quick_sort_first(arr[i+1:])
    left.append(arr[i])
    result = left + right

    return result


def quick_sort_last(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[-1]
    i = -1
    for j in range(0, len(arr)):
        if arr[j] <= pivot:
            i += 1
            arr[j], arr[i] = arr[i], arr[j]

    arr[i+1], arr[-1] = arr[-1], arr[i+1]

    left = quick_sort_last(arr[:i])
    right = quick_sort_last(arr[i+1:])
    left.append(arr[i])
    result = left + right

    return result


def quick_sort(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)
        quick_sort(arr, low, pivot - 1)
        quick_sort(arr, pivot + 1, high)

    return arr


def partition(arr, low, high):
    if len(arr) <= 1:
        return arr

    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[j], arr[i] = arr[i], arr[j]

    arr[high], arr[i+1] = arr[i+1], arr[high]

    return (i+1)


if __name__ == "__main__":
    unsorted_arr = [22, 20, 8, 10, 44, 7, 32, 1, 9 ,15]
    sorted_arr = quick_sort(unsorted_arr, 0, len(unsorted_arr)-1)
    print(sorted_arr)
