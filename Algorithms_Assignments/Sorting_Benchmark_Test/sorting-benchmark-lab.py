import random
from time import perf_counter

def insertion_sort(data):
    result=list(data)
    for i in range(1,len(result)):
        value=result[i]; j=i
        while j and result[j-1]>value:
            result[j]=result[j-1]; j-=1
        result[j]=value
    return result

def merge_sort(data):
    if len(data)<2:return list(data)
    mid=len(data)//2
    left,right=merge_sort(data[:mid]),merge_sort(data[mid:])
    out=[]; i=j=0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:out.append(left[i]);i+=1
        else:out.append(right[j]);j+=1
    return out+left[i:]+right[j:]

def quick_sort(data):
    if len(data)<2:return list(data)
    pivot=data[len(data)//2]
    less=[v for v in data if v<pivot]
    same=[v for v in data if v==pivot]
    greater=[v for v in data if v>pivot]
    return quick_sort(less)+same+quick_sort(greater)

def benchmark():
    methods={"Insertion":insertion_sort,"Merge":merge_sort,"Quick":quick_sort,"Built-in":sorted}
    for size in (500,1500,3000,6000):
        source=list(range(size)); random.shuffle(source)
        print(f"\nElements: {size}")
        for label,method in methods.items():
            start=perf_counter(); answer=method(source); elapsed=perf_counter()-start
            assert answer==sorted(source)
            print(f"{label:10} {elapsed:.6f}s")

if __name__=="__main__": benchmark()
