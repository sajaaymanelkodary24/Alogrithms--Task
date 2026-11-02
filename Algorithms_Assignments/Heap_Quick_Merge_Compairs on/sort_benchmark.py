import random
from time import perf_counter
import heapq

def heap_sort(values):
    heap = list(values)
    heapq.heapify(heap)
    return [heapq.heappop(heap) for _ in range(len(heap))]

def quick_sort(values):
    if len(values) < 2:
        return list(values)
    pivot = values[len(values)//2]
    lower, equal, upper = [], [], []
    for value in values:
        (lower if value < pivot else upper if value > pivot else equal).append(value)
    return quick_sort(lower) + equal + quick_sort(upper)

def merge_sort(values):
    width, result = 1, list(values)
    while width < len(result):
        merged = []
        for start in range(0, len(result), width*2):
            left, right = result[start:start+width], result[start+width:start+2*width]
            i = j = 0
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    merged.append(left[i]); i += 1
                else:
                    merged.append(right[j]); j += 1
            merged.extend(left[i:]); merged.extend(right[j:])
        result, width = merged, width*2
    return result

def measure(algorithm, data):
    start = perf_counter()
    output = algorithm(data)
    return perf_counter()-start, output

if __name__ == "__main__":
    algorithms = {"Heap Sort":heap_sort,"Quick Sort":quick_sort,"Merge Sort":merge_sort}
    for size in (100, 500, 1000, 2000):
        sample = [random.randrange(10001) for _ in range(size)]
        print(f"\nInput size: {size}")
        for name, function in algorithms.items():
            elapsed, output = measure(function, sample)
            assert output == sorted(sample)
            print(f"{name:12} {elapsed:.6f}s")
