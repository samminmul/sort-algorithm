#선택, 삽입, 버블, 병합, 퀵, 힙

def selection(arr, check=False):
    if check: print("---selcection sort---")
    
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        
        if check: print(f"swap {i}, {min_idx}: {arr}")
        
    if check: print("---selcection sort end---")
    return arr

def insertion(arr, check=False):
    if check: print("---insetion sort---")

    for i in range(len(arr)):
        

arr = [1, 5, 3, 2, 4]
sorted_arr = selection(arr, check=True)
print(sorted_arr)
