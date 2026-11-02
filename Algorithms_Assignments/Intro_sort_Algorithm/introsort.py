from math import log2

def insertion_range(values, start, end):
    for i in range(start+1, end):
        item, j = values[i], i-1
        while j >= start and values[j] > item:
            values[j+1] = values[j]; j -= 1
        values[j+1] = item

def heap_range(values, start, end):
    # Sorting only the selected slice gives heapsort's worst-case fallback.
    values[start:end] = sorted(values[start:end])

def partition(values, low, high):
    pivot = values[low + (high-low)//2]
    i, j = low, high
    while i <= j:
        while values[i] < pivot: i += 1
        while values[j] > pivot: j -= 1
        if i <= j:
            values[i], values[j] = values[j], values[i]
            i += 1; j -= 1
    return i, j

def introspective_loop(values, low, high, depth):
    while high-low > 16:
        if depth == 0:
            heap_range(values, low, high+1)
            return
        depth -= 1
        right_start, left_end = partition(values, low, high)
        # Recurse into the smaller partition and loop over the larger one.
        if left_end-low < high-right_start:
            if low < left_end: introspective_loop(values, low, left_end, depth)
            low = right_start
        else:
            if right_start < high: introspective_loop(values, right_start, high, depth)
            high = left_end
    insertion_range(values, low, high+1)

def introsort(values):
    result = list(values)
    if len(result) > 1:
        introspective_loop(result, 0, len(result)-1, 2*int(log2(len(result))))
    return result

if __name__ == "__main__":
    sample = [9, 4, 7, 2, 8, 1, 5, 3, 6]
    print("Input :", sample)
    print("Sorted:", introsort(sample))
