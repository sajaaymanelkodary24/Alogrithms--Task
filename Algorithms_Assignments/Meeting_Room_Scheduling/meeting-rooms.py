import heapq

def minimum_rooms(meetings):
    if any(start > end for start, end in meetings):
        raise ValueError("Meeting start must not be after its end")
    active_ends = []
    for start, end in sorted(meetings):
        while active_ends and active_ends[0] <= start:
            heapq.heappop(active_ends)
        heapq.heappush(active_ends, end)
    return len(active_ends)

if __name__ == "__main__":
    schedule = [(0,30),(5,10),(15,20),(35,40)]
    print("Meetings:", schedule)
    print("Minimum rooms required:", minimum_rooms(schedule))
