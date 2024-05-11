from random import randrange
from time import time
import matplotlib.pyplot as plt
import numpy as np
from sort_algorithms import sort_collection


sorts = sort_collection[:-1] #counting_sort2는 일단 제외
sort_times = [[0]*10 for _ in range(len(sorts))]

lengths_of_arrs_to_sort = [i*1000 for i in range(1, len(sort_times[0]) + 1)]
REPEAT = 5
for _ in range(REPEAT):
    for i in range(len(lengths_of_arrs_to_sort)):
        arr = [randrange(100) for _ in range(lengths_of_arrs_to_sort[i])]

        for j in range(len(sorts)):
            arr_to_sort = arr.copy()
            timestamp = time()
            sorts[j](arr_to_sort)
            sort_time = time() - timestamp

            print(lengths_of_arrs_to_sort[i], sort_time, sorts[j].__name__, sep=" ; ")
            sort_times[j][i] += sort_time/REPEAT


for i in range(len(sorts)):
    plt.plot(lengths_of_arrs_to_sort, sort_times[i], label=sorts[i].__name__)

plt.xlabel("array length")
plt.ylabel("spent time")
plt.legend()
plt.show()