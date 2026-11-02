import random
from time import perf_counter

class DaryMaxHeap:
    def __init__(self, degree):
        if degree < 2:
            raise ValueError("Heap degree must be at least 2")
        self.degree, self.items = degree, []

    def push(self, value):
        self.items.append(value)
        child = len(self.items) - 1
        while child:
            parent = (child - 1) // self.degree
            if self.items[parent] >= value:
                break
            self.items[child] = self.items[parent]
            child = parent
        self.items[child] = value

    def pop(self):
        if not self.items:
            raise IndexError("pop from empty heap")
        maximum = self.items[0]
        tail = self.items.pop()
        if self.items:
            index, size = 0, len(self.items)
            while True:
                first = self.degree * index + 1
                if first >= size:
                    break
                last = min(first + self.degree, size)
                best = max(range(first, last), key=self.items.__getitem__)
                if self.items[best] <= tail:
                    break
                self.items[index] = self.items[best]
                index = best
            self.items[index] = tail
        return maximum

def benchmark(degree, values):
    heap = DaryMaxHeap(degree)
    t0 = perf_counter()
    for value in values:
        heap.push(value)
    insert_seconds = perf_counter() - t0
    t0 = perf_counter()
    while heap.items:
        heap.pop()
    return insert_seconds, perf_counter() - t0

if __name__ == "__main__":
    sample = [random.randrange(1, 10001) for _ in range(20000)]
    for degree in (2, 3, 4, 8):
        add, remove = benchmark(degree, sample)
        print(f"{degree}-ary heap | insert {add:.5f}s | remove {remove:.5f}s")
