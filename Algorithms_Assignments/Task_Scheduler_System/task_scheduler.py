import heapq
from itertools import count

class TaskScheduler:
    def __init__(self):
        self._queue=[]
        self._sequence=count()

    def add(self, title, priority):
        heapq.heappush(self._queue,(-int(priority),next(self._sequence),title))

    def execute_next(self):
        if not self._queue:return None
        priority,_,title=heapq.heappop(self._queue)
        return title,-priority

    def __len__(self):return len(self._queue)

def main():
    scheduler=TaskScheduler()
    print("Commands: INSERT, EXTRACT-MAX, EXIT")
    while True:
        command=input("> ").strip().upper()
        if command=="INSERT":
            title=input("Task title: ").strip()
            try:priority=int(input("Priority: "))
            except ValueError:print("Priority must be an integer.");continue
            scheduler.add(title,priority);print("Task added.")
        elif command=="EXTRACT-MAX":
            task=scheduler.execute_next()
            print(f"Executing: {task[0]} (priority {task[1]})" if task else "No pending tasks.")
        elif command=="EXIT":break
        else:print("Unknown command.")

if __name__=="__main__":main()
