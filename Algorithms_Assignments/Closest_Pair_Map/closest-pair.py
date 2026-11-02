from math import radians, sin, cos, asin, sqrt
from itertools import combinations
from time import perf_counter

LOCATIONS = [
    ("Cafe A", 30.0444, 31.2357), ("Cafe B", 30.0500, 31.2400),
    ("Cafe C", 30.0600, 31.2200), ("Cafe D", 30.0300, 31.2500),
    ("Cafe E", 30.0470, 31.2320),
]

def haversine(p, q):
    lat1, lon1, lat2, lon2 = map(radians, (p[1], p[2], q[1], q[2]))
    a = sin((lat2-lat1)/2)**2 + cos(lat1)*cos(lat2)*sin((lon2-lon1)/2)**2
    return 2 * 6371.0 * asin(sqrt(a))

def brute_force(points):
    if len(points) < 2:
        raise ValueError("At least two locations are required")
    return min((haversine(a, b), a[0], b[0]) for a, b in combinations(points, 2))

def divide_and_conquer(points):
    # Recursive split on latitude; the strip is checked for cross-boundary pairs.
    if len(points) <= 3:
        return brute_force(points)
    ordered = sorted(points, key=lambda item: item[1])
    middle = len(ordered) // 2
    left_result = divide_and_conquer(ordered[:middle])
    right_result = divide_and_conquer(ordered[middle:])
    best = min(left_result, right_result, key=lambda result: result[0])
    split_lat = (ordered[middle-1][1] + ordered[middle][1]) / 2
    # One degree of latitude is approximately 111 km.
    candidates = [p for p in ordered if abs(p[1] - split_lat) * 111 < best[0]]
    for a, b in combinations(candidates, 2):
        distance = haversine(a, b)
        if distance < best[0]:
            best = (distance, a[0], b[0])
    return best

if __name__ == "__main__":
    for label, algorithm in (("Brute force", brute_force), ("Divide and conquer", divide_and_conquer)):
        started = perf_counter()
        answer = algorithm(LOCATIONS)
        print(f"{label}: {answer[1]} / {answer[2]} = {answer[0]:.3f} km ({perf_counter()-started:.6f}s)")
