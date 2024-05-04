from random import randrange
from time import time


#정렬: 선택, 삽입, 버블, 병합, 퀵, 힙, 카운팅, 인트로

def swap(arr, i, j, check=False):
    arr[i], arr[j] = arr[j], arr[i]
    if check:
        print(f"swap {i}, {j} -> {arr}")


def selection_sort(arr):
    
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        swap(arr, i, min_idx)


def insertion_sort(arr):

    for i in range(1, len(arr)):
        while arr[i - 1] > arr[i] and i > 1:
            swap(arr, i, i - 1)
            i -= 1


def bubble_sort(arr):

    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                swap(arr, j, j + 1)


def merge(arr, start, half, end):
    i1, i2 = start, half + 1
    tmp = []
    while i1 <= half and i2 <= end:
        if arr[i1] < arr[i2]:
            tmp.append(arr[i1])
            i1 += 1
        else:
            tmp.append(arr[i2])
            i2 += 1

    for i in range(i1, half + 1):
        tmp.append(arr[i])
    for i in range(i2, end + 1):
        tmp.append(arr[i])

    for i in range(len(tmp)):
        arr[start + i] = tmp[i]

def merge_sort(arr, start, end):
    if start >= end: 
        return
    
    half = start + (end - start)//2
    merge_sort(arr, start, half)
    merge_sort(arr, half + 1, end)
    merge(arr, start, half, end)
    

def partition(arr, start, end):
    pivot, piv_idx = arr[start], start
    low, high = start, end + 1
    while True:

        while True:
            low += 1
            if low > end or arr[low] > pivot:
                break
        while True:
            high -= 1
            if high <= start or arr[high] < pivot:
                break
        
        if low >= high:
            break
        swap(arr, low, high)

    swap(arr, piv_idx, low - 1)
    piv_idx = low - 1

    return piv_idx

def quick_sort(arr, start, end):
    if start >= end:
        return
    
    piv_idx = partition(arr, start, end)
    quick_sort(arr, start, piv_idx - 1)
    quick_sort(arr, piv_idx + 1, end)
    
    
arr = [randrange(0, 100) for _ in range(20)]

merge_sort(arr, 0, len(arr) - 1)
print(arr)
