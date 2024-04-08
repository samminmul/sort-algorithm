#선택, 삽입, 버블, 병합, 퀵, 힙, 카운팅, 인트로


def swap(arr, i, j, check):
    arr[i], arr[j] = arr[j], arr[i]
    if check:
        print(f"swap {i}, {j} -> {arr}")

def selection(arr, check=False):
    if check: print("---selcection sort---")
    
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        swap(arr, i, min_idx, check)
        
    return arr

def insertion(arr, check=False):
    if check: print("---insetion sort---")

    for i in range(1, len(arr)):
        while arr[i - 1] > arr[i] and i > 1:
            swap(arr, i, i - 1, check)
            i -= 1
        
    return arr

def bubble(arr, check=False):
    if check: print("---bubble sort---")
    
    for _ in range(len(arr)):
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                swap(arr, i, i + 1, check)

    return arr

            
arr = [5, 2, 4, 3, 1]
sorted_arr = bubble(arr, check=True)
print(sorted_arr)
