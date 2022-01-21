"""
Bubble Sort Algorithm

*   20/01/2022  Initial Code
*   21/01/2022  Added recursive method

"""

def bubble_sort(arr=[]):

    n = len(arr)
    for i in range(n):
        for j in range(0, n-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr


def recursive_bubble_sort(arr=None, arr_len=None):
    if arr_len == 1:
        return

    for i in range(arr_len-1):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]

    recursive_bubble_sort(arr, arr_len - 1)
    return arr


if __name__ == "__main__":
    unsorted_arr = [9, 3, 5, 1, 2, 10, 69, 29, 44]
    sorted_arr = bubble_sort(unsorted_arr)
    recursive_sorted_arr = recursive_bubble_sort(unsorted_arr, len(unsorted_arr))
    print(sorted_arr)
    print(recursive_sorted_arr)
