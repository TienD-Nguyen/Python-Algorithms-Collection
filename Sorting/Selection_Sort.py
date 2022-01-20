def selection_sort(arr=[]):
    for i in range(len(arr) - 1):
        min = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min]:
                min = j

        if min != i:
            arr[i], arr[min] = arr[min], arr[i]

    return arr


def selectionsort(arr=[]):
    sorted_arr = []

    while arr:
        min = arr[0]
        for element in arr:
            min = element if element < min else min

        sorted_arr.append(min)
        arr.remove(min)

    return sorted_arr


if __name__ == "__main__":
    unsorted_arr = [9, 3, 5, 1, 2, 10, 69, 29, 44]
    sorted_arr = selectionsort(unsorted_arr)
    print(sorted_arr)
