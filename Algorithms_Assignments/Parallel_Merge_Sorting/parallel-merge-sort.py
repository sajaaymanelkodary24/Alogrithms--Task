import random
from time import perf_counter
from concurrent.futures import ProcessPoolExecutor
import heapq

def merge_sort(values):
    if len(values) < 2: return list(values)
    middle = len(values)//2
    left, right = merge_sort(values[:middle]), merge_sort(values[middle:])
    output=[]; i=j=0
    while i<len(left) and j<len(right):
        if left[i] <= right[j]: output.append(left[i]); i+=1
        else: output.append(right[j]); j+=1
    return output+left[i:]+right[j:]

def parallel_sort(values, workers=2):
    if workers < 1: raise ValueError("workers must be positive")
    if len(values) < 2 or workers == 1: return merge_sort(values)
    chunk_size = (len(values)+workers-1)//workers
    chunks = [values[i:i+chunk_size] for i in range(0,len(values),chunk_size)]
    with ProcessPoolExecutor(max_workers=workers) as pool:
        sorted_chunks = list(pool.map(merge_sort,chunks))
    return list(heapq.merge(*sorted_chunks))

if __name__ == "__main__":
    numbers=[random.randrange(100000) for _ in range(50000)]
    for count in (1,2,4):
        started=perf_counter(); output=parallel_sort(numbers,count)
        print(f"{count} process(es): {perf_counter()-started:.3f}s | correct={output==sorted(numbers)}")
