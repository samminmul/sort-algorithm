from random import randrange
from time import time


#정렬: 선택, 삽입, 버블, 병합, 퀵, 힙, 카운팅, 인트로

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
    if check: print("---merge sort---")
    
    if len(arr) <= 1:
        return arr

    half = len(arr) // 2
    arr1, arr2 = arr[:half], arr[half:]
    arr1 = merge_sort(arr1)
    arr2 = merge_sort(arr2)
    
    merged_arr = []
    i1, i2 = 0, 0
    while i1 < len(arr1) and i2 < len(arr2):
        if arr1[i1] < arr2[i2]:
            merged_arr.append(arr1[i1])
            i1 += 1
        else:
            merged_arr.append(arr2[i2])
            i2 += 1

    merged_arr += arr1[i1:]
    merged_arr += arr2[i2:]
    
    return merged_arr    
    
def quick_sork(arr, check=False):
    if check: print("---quick sort---")

    pivot = arr[0]

    
arr = [1, 3, 2, 4, 5]

sorted_arr = merge_sort(arr)
print(arr)
print(sorted_arr)
