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


def recursive_insertion_sort(arr, arr_length):
    if arr_length <= 1:
        return

    recursive_insertion_sort(arr, arr_length - 1)

    last_element = arr[arr_length-1]
    j = arr_length - 2
    while j >= 0 and arr[j] > last_element:
        arr[j+1] = arr[j]
        j -= 1

    arr[j+1] = last_element

    return arr


if __name__ == "__main__":
    unsorted_arr = [9, 3, 5, 1, 2, 10, 69, 29, 44]

    sorted_arr = insertion_sort(unsorted_arr)
    recursive_sorted_arr = recursive_insertion_sort(unsorted_arr, len(unsorted_arr))

    print(sorted_arr)
    print(recursive_sorted_arr)
