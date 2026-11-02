import heapq
from itertools import count

ARRIVALS = [(1, "Customer A"), (2, "Customer B"), (3, "Customer C"), (5, "Customer D")]

def run_simulation(arrivals, teller_count=2, service_duration=3):
    if teller_count < 1 or service_duration < 0:
        raise ValueError("Invalid simulation settings")
    events = [(when, next(order), customer) for when, customer in arrivals]
    heapq.heapify(events)
    available = [0] * teller_count
    report = []
    while events:
        arrival, _, customer = heapq.heappop(events)
        teller = min(range(teller_count), key=available.__getitem__)
        start = max(arrival, available[teller])
        finish = start + service_duration
        available[teller] = finish
        report.append((customer, arrival, teller + 1, start, finish))
    return report

if __name__ == "__main__":
    for customer, arrival, teller, start, finish in run_simulation(ARRIVALS):
        print(f"{customer}: arrives {arrival}, teller {teller}, starts {start}, finishes {finish}")
