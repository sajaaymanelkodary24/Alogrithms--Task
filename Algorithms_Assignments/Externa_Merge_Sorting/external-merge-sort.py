import heapq
import os
import tempfile
from contextlib import ExitStack

def external_sort(source, destination, chunk_size=1000):
    if chunk_size < 1:
        raise ValueError("chunk_size must be positive")
    temp_paths = []
    try:
        with open(source, encoding="utf-8") as incoming:
            while True:
                values = []
                for _ in range(chunk_size):
                    line = incoming.readline()
                    if not line:
                        break
                    values.append(int(line.strip()))
                if not values:
                    break
                values.sort()
                handle = tempfile.NamedTemporaryFile(mode="w", delete=False, encoding="utf-8")
                temp_paths.append(handle.name)
                with handle:
                    handle.writelines(f"{value}\n" for value in values)
        with ExitStack() as stack, open(destination, "w", encoding="utf-8") as output:
            streams = [stack.enter_context(open(path, encoding="utf-8")) for path in temp_paths]
            merged = heapq.merge(*(map(int, stream) for stream in streams))
            for value in merged:
                output.write(f"{value}\n")
    finally:
        for path in temp_paths:
            if os.path.exists(path):
                os.remove(path)

if __name__ == "__main__":
    if not os.path.exists("input.txt"):
        with open("input.txt", "w", encoding="utf-8") as sample:
            sample.writelines(f"{number}\n" for number in [9, 2, 7, 1, 5, 3, 8, 4, 6])
    external_sort("input.txt", "sorted.txt", chunk_size=3)
    print("Sorted values saved to sorted.txt")
