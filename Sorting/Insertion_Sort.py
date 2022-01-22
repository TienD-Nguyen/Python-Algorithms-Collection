"""
Insertion Sort Algorithm

*   21/01/2022  Initial Code
*   22/01/2022  Added recursive method

"""

def insertion_sort(arr=[]):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1

        arr[j+1] = key

    return arr


def recursive_insertion_sort(arr=[]):
    n = len(arr)
    if n <= 1:
        return

    recursive_insertion_sort(arr, n - 1)

    last_element = arr[n-1]
    j = n - 2
    while j >= 0 and arr[j] > last_element:
        arr[j+1] = arr[j]
        j -= 1

    arr[j+1] = last_element


if __name__ == "__main__":
    unsorted_arr = [9, 3, 5, 1, 2, 10, 69, 29, 44]
    sorted_arr = insertion_sort(unsorted_arr)
    print(sorted_arr)
