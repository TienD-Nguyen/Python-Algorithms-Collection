def selection_sort(arr=[]):
    for i in range(len(arr) - 1):
        min = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min]:
                min = j

        if min != i:
            arr[i], arr[min] = arr[min], arr[i]

    return arr

if __name__ == "__main__":
    unsorted_arr = [9, 2, 5, 1, 4]
    sorted_arr = selection_sort(unsorted_arr)
    print(sorted_arr)
