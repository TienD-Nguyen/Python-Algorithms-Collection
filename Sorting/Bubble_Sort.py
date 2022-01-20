def selection_sort(arr=[]):

    n = len(arr)
    for i in range(n):
        for j in range(0, n-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr



if __name__ == "__main__":
    unsorted_arr = [9, 3, 5, 1, 2, 10, 69, 29, 44]
    sorted_arr = selection_sort(unsorted_arr)
    print(sorted_arr)
