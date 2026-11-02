import heapq

def merge_sorted_lists(sequences):
    # Heap entries include the source index so equal values remain comparable.
    heap = []
    iterators = [iter(sequence) for sequence in sequences]
    for source, iterator in enumerate(iterators):
        first = next(iterator, None)
        if first is not None:
            heapq.heappush(heap, (first, source))
    merged = []
    while heap:
        value, source = heapq.heappop(heap)
        merged.append(value)
        following = next(iterators[source], None)
        if following is not None:
            heapq.heappush(heap, (following, source))
    return merged

if __name__ == "__main__":
    collections = [[1, 4, 7], [2, 5, 8], [3, 6, 9], [0, 10]]
    print("Merged sequence:", merge_sorted_lists(collections))
