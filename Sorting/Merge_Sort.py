"""
Merge Sort Algorithm

*   23/01/2022  Initial code
*   26/01/2022  Added an iterative method

"""

# ---------------Top-Down (Recursive Method) ------------------
def merge_sort(arr=[]):
    if len(arr) <= 1:
        return arr

    mid = int(len(arr) / 2)

    left, right = merge_sort(arr[:mid]), merge_sort(arr[mid:])

    return merge(left, right)


def merge(left=[], right=[]):
    i = j = 0
    result = []

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        elif left[i] > right[j]:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


# ---------------Bottom-Up (Iterative Method) ----------------
def iterative_merge_sort(arr=[]):
    n = len(arr)
    subarray_length = 1

    while subarray_length < n:
        left = 0
        while left < n:
            right = min(left + (subarray_length * 2 - 1), n-1)
            mid = (left + right) // 2
            if subarray_length > (n//2):
                mid = right - (n % subarray_length)
            iterative_merge(arr, left, mid, right)
            left += subarray_length * 2

        subarray_length *= 2

    return arr


def iterative_merge(arr, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid
    left_sub_array = [0] * n1
    right_sub_array = [0] * n2

    for i in range(0, n1):
        left_sub_array[i] = arr[left + i]
    for i in range(0, n2):
        right_sub_array[i] = arr[mid + i + 1]

    i, j, k = 0, 0, left
    while i < n1 and j < n2:
        if left_sub_array[i] < right_sub_array[j]:
            arr[k] = left_sub_array[i]
            i += 1
        else:
            arr[k] = right_sub_array[j]
            j += 1
        k += 1

    while i < len(left_sub_array):
        arr[k] = left_sub_array[i]
        i += 1
        k += 1

    while j < len(right_sub_array):
        arr[k] = right_sub_array[j]
        j += 1
        k += 1



if __name__ == "__main__":
    unsorted_arr = [9, 3, 5, 1, 2, 10, 69, 29, 44]
    sorted_arr = iterative_merge_sort(unsorted_arr)
    print(sorted_arr)
