import heapq
import json
from collections import Counter
from itertools import count

def create_tree(message):
    frequencies = Counter(message)
    serial = count()
    queue = [(freq, next(serial), char) for char, freq in frequencies.items()]
    heapq.heapify(queue)
    if not queue:
        return None
    while len(queue) > 1:
        f1, _, left = heapq.heappop(queue)
        f2, _, right = heapq.heappop(queue)
        heapq.heappush(queue, (f1+f2, next(serial), (left, right)))
    return queue[0][2]

def make_codes(tree):
    codes = {}
    def visit(node, prefix):
        if isinstance(node, str):
            codes[node] = prefix or "0"
            return
        left, right = node
        visit(left, prefix+"0")
        visit(right, prefix+"1")
    if tree is not None:
        visit(tree, "")
    return codes

def encode(message, codes):
    return "".join(codes[char] for char in message)

def decode(bit_string, codes):
    reverse = {code: char for char, code in codes.items()}
    result, buffer = [], ""
    for bit in bit_string:
        buffer += bit
        if buffer in reverse:
            result.append(reverse[buffer]); buffer = ""
    if buffer:
        raise ValueError("Invalid encoded bit stream")
    return "".join(result)

if __name__ == "__main__":
    try:
        with open("input.txt", encoding="utf-8") as source:
            message = source.read()
    except FileNotFoundError:
        message = "Huffman coding compresses repeated symbols efficiently."
        with open("input.txt", "w", encoding="utf-8") as source:
            source.write(message)
    codes = make_codes(create_tree(message))
    bits = encode(message, codes)
    restored = decode(bits, codes) if codes else ""
    with open("compressed.json", "w", encoding="utf-8") as target:
        json.dump({"codes":codes,"bits":bits,"characters":len(message)}, target, ensure_ascii=False, indent=2)
    print("Original characters:",len(message),"Encoded bits:",len(bits),"Decoded correctly:",restored==message)
