"""
Heap Sort Algorithm

*   04/02/2022  Initial Code

"""

def heapify(arr: list, n: int, i: int):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[largest] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr: list):
    N = len(arr)

    for i in range(N//2 - 1, -1, -1):
        heapify(arr, N, i)

    for i in range(N-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)

    return arr

if __name__ == "__main__":
    arr = [3, 9, 2, 1, 4, 5, 10]
    heap_arr = heap_sort(arr)
    print(heap_arr)
