import heapq

class RunningMedian:
    def __init__(self):
        self.lower = []  # max heap represented by negative values
        self.upper = []  # min heap

    def add(self, value):
        if not self.lower or value <= -self.lower[0]:
            heapq.heappush(self.lower, -value)
        else:
            heapq.heappush(self.upper, value)
        if len(self.lower) > len(self.upper)+1:
            heapq.heappush(self.upper, -heapq.heappop(self.lower))
        elif len(self.upper) > len(self.lower):
            heapq.heappush(self.lower, -heapq.heappop(self.upper))
        return self.median()

    def median(self):
        if not self.lower: raise ValueError("No values have been added")
        if len(self.lower) > len(self.upper): return float(-self.lower[0])
        return (-self.lower[0]+self.upper[0])/2

if __name__ == "__main__":
    tracker=RunningMedian()
    raw=input("Enter numbers separated by spaces: ").strip()
    for token in raw.split():
        print(f"After {token}: median = {tracker.add(float(token))}")
