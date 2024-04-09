#선택, 삽입, 버블, 병합, 퀵, 힙, 카운팅, 인트로


def swap(arr, i, j, check=False):
    arr[i], arr[j] = arr[j], arr[i]
    if check:
        print(f"swap {i}, {j} -> {arr}")

def selection_sort(arr, check=False):
    if check: print("---selcection sort---")
    
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        swap(arr, i, min_idx, check)
        
    return arr

def insertion_sort(arr, check=False):
    if check: print("---insetion sort---")

    for i in range(1, len(arr)):
        while arr[i - 1] > arr[i] and i > 1:
            swap(arr, i, i - 1, check)
            i -= 1
        
    return arr

def bubble_sort(arr, check=False):
    if check: print("---bubble sort---")
    
    for i in range(len(arr)):
        for j in range(len(arr) - i-1):
            if arr[j] > arr[j + 1]:
                swap(arr, j, j + 1, check)

    return arr

def merge_sort(arr, check=False):
    
    
    half = len(arr) // 2
    arr1, arr2 = arr[:half], arr[half:]
    merge_sort(arr1)
    
    
arr = [5, 2, 4, 3, 1]
sorted_arr = bubble_sort(arr, check=True)
print(swap.__name__)
print(sorted_arr)
