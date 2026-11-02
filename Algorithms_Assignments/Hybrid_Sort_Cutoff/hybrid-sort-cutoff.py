import random
from time import perf_counter

def insertion_sort(items):
    for index in range(1, len(items)):
        current, position = items[index], index
        while position and items[position-1] > current:
            items[position] = items[position-1]
            position -= 1
        items[position] = current
    return items

def merge(left, right):
    output, i, j = [], 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            output.append(left[i]); i += 1
        else:
            output.append(right[j]); j += 1
    return output + left[i:] + right[j:]

def hybrid_sort(items, cutoff):
    if len(items) <= cutoff:
        return insertion_sort(list(items))
    middle = len(items)//2
    return merge(hybrid_sort(items[:middle], cutoff), hybrid_sort(items[middle:], cutoff))

if __name__ == "__main__":
    data = [random.randrange(100000) for _ in range(5000)]
    for threshold in (4, 8, 16, 24, 32, 48, 64):
        started = perf_counter()
        result = hybrid_sort(data, threshold)
        print(f"Cutoff {threshold:2}: {perf_counter()-started:.5f}s | valid={result==sorted(data)}")
