#정렬: 선택, 삽입, 버블, 병합, 퀵, 힙, 카운팅

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
    

class Heap:
    def __init__(self, arr) -> None:
        self.heap = [0]
        for i in arr:
            self.insert(i)

    def getsize(self):
        return len(self.heap) - 1
    
    def heapify(self, i):
        while 1 < i <= self.getsize() and self.heap[i] < self.heap[i//2]:
            swap(self.heap, i, i//2)
            i //= 2
        while True:
            if i*2 > self.getsize():
                return
            elif i*2 == self.getsize():
                if self.heap[i] > self.heap[i*2]:
                    swap(self.heap, i, i*2)
                    i *= 2
                else:
                    return
            else:
                if self.heap[i*2] > self.heap[i*2 + 1] and self.heap[i] > self.heap[i*2 + 1]:
                    swap(self.heap, i, i*2 + 1)
                    i = i*2 + 1
                elif self.heap[i*2] <= self.heap[i*2 + 1] and self.heap[i] > self.heap[i*2]:
                    swap(self.heap, i, i*2)
                    i *= 2
                else:
                    return

    def insert(self, value: int):
        self.heap.append(value)
        self.heapify(self.getsize())
        
    def pophead(self):
        swap(self.heap, 1, self.getsize())
        head = self.heap.pop()
        self.heapify(1)

        return head

def heap_sort(arr):
    heap = Heap(arr)
    rslt = []
    for _ in range(heap.getsize()):
        rslt.append(heap.pophead())

    return rslt


def counting_sort1(arr):
    count = [0] * (max(arr) + 1)
    for i in arr:
        count[i] += 1

    rslt = []
    for i in range(len(count)):
        for _ in range(count[i]):
            rslt.append(i)

    return rslt

def counting_sort2(arr): #누적합 이용
    count = [0] * (max(arr) + 1)
    for i in arr:
        count[i] += 1

    for i in range(1, len(count)):
        count[i] += count[i-1]

    rslt = [0] * (len(arr))
    for num in arr:
        idx = count[num]
        rslt[idx - 1] = num
        count[num] -= 1

    return rslt