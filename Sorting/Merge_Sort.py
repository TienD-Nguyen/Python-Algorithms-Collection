"""
Merge Sort Algorithm

*   23/01/2022  Initial code

"""

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


if __name__ == "__main__":
    unsorted_arr = [9, 3, 5, 1, 2, 10, 69, 29, 44]
    sorted_arr = merge_sort(unsorted_arr)
    print(sorted_arr)
