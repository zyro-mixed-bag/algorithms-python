#!/usr/bin/python

def heapSort(a, n):
    heapify(a,n)  
    end = n - 1
    while (end > 0):
        a[end], a[0] = a[0], a[end]
        end -= 1
        siftDown(a, 0, end)
    return a
        
        
def heapify(a, n):
    start = int((n - 2) / 2)
    while(start >= 0):
        siftDown(a, start, n-1)
        start -= 1
        

def siftDown(a, start, end):
    root = start
    
    while(root*2 + 1 <= end):
        child = root*2 + 1
        
        if child+1 <= end and a[child] < a[child+1]:
            child+=1
        
        if a[root] < a[child]:
            a[root], a[child] = a[child], a[root]
            root = child
            
        else:
            break
    
    
def main():
    a = [4, 3, 1, 2, 0]
    a = heapSort(a, len(a))
    print(a)
    
if __name__ == '__main__':main()