import sys
from random import randrange, shuffle
from time import time
from typing import Callable
import matplotlib.pyplot as plt
from sort_algorithms import bubble_sort, insertion_sort, selection_sort, merge_sort, \
                            heap_sort, quick_sort, counting_sort, counting_sort2
RECURSION_LIMIT = 100000000
sys.setrecursionlimit(RECURSION_LIMIT)
plt.rcParams['font.family'] ='Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False


class ListGenerator:
    def _swap(self, arr: list, i: int, j: int) -> None:
        arr[i], arr[j] = arr[j], arr[i]

    def generate_random_list(self, length: int) -> list[int]:
        return shuffle([i for i in range(length)])

    def generate_random_list_allowing_overlap(self, length: int, min_value: int, max_value: int) -> list[int]:
        return [randrange(min_value, max_value + 1) for _ in range(length)]

    def generate_sorted_list(self, length: int) -> list[int]:
        return [i for i in range(length)]

    def generate_reversed_list(self, length: int) -> list[int]:
        return [i for i in range(length-1, -1, -1)]

    def generate_almost_sorted_list(self, length: int, shuffle_count: int) -> list[int]:
        rslt = self.generate_sorted_list(length)
        for _ in range(shuffle_count):
            self._swap(rslt, randrange(length), randrange(length))
        return rslt


def builtin_sort(arr: list) -> None:
    return sorted(arr)

def measure_sorting_time(sort_algorithm: Callable[[list], list|None], arr: list) -> int:
    timestamp = time()
    sort_algorithm(arr)
    sort_time = time() - timestamp

    return sort_time

def log(repeat: int, arr_len: int, spent_time: float, algorithm_name: str) -> None:
    print(repeat, arr_len, spent_time, algorithm_name, sep=" ; ")


ARRLEN_START, ARRLEN_STOP, ARRLEN_STEP = 1000, 2501, 500
sort_algorithms: list[Callable[[list], list|None]] = [bubble_sort, insertion_sort, 
    selection_sort, merge_sort, heap_sort, quick_sort, counting_sort, builtin_sort]

arr_lengths = [i for i in range(ARRLEN_START, ARRLEN_STOP, ARRLEN_STEP)]
spent_times = [[0]*len(arr_lengths) for _ in range(len(sort_algorithms))]
lg = ListGenerator()


REPEATS = 5
for repeat in range(1, REPEATS + 1):
    for i in range(len(arr_lengths)): #각각의 리스트 길이에 대해(x축)
        arr = lg.generate_almost_sorted_list(arr_lengths[i], 3)

        for j in range(len(sort_algorithms)): #각 정렬 알고리즘에 대해 시간 측정
            arr_to_sort = arr.copy()
            sort_time = measure_sorting_time(sort_algorithms[j], arr_to_sort)

            log(repeat, arr_lengths[i], sort_time, sort_algorithms[j].__name__,)
            spent_times[j][i] += sort_time/REPEATS #평균 정렬 시간 계산을 위해 반복 횟수로 나눔


for i in range(len(sort_algorithms)):
    plt.plot(arr_lengths, spent_times[i], label=sort_algorithms[i].__name__)

plt.xlabel("리스트의 길이")
plt.ylabel("정렬 시간(초)")
plt.title("거의 정렬된 리스트에 대한 정렬 속도") #이곳에 그래프 제목 입력
plt.legend()
plt.show()