import sys

def quickSort(A, p, r):
    flag = 0
    i=p
    while(i<=r-1):
        if A[i] != A[i+1]:
            flag = 1
            break
        i += 1
        
    if flag == 0:
        return
        
    if p<r:
        q, count = partition(A,p,r)
        quickSort(A, p, q-1)
        quickSort(A, q+count, r)
        
def partition(A, p ,r):
    x = A[r]
    i = p-1
    
    j=p
    while(j<=r-1):
        if A[j] < x:
            i += 1
            A[i], A[j] = A[j], A[i]

        j+=1
    
    A[i+1], A[r] = A[r], A[i+1]
    
    k = p
    pivotIndex = i+1
    count = 0
    while(k<= r):
        if A[k] == x:
            del A[k]
            A.insertNode(pivotIndex, x)
            count += 1
        k+=1
            
    return i+1, count


def main():
    myInput = sys.stdin.readline()
    A = myInput.split()
    A = [int(x) for x in A]
#    A = [6,5,4,6,1,5,6,6]
    quickSort(A, 0, len(A)-1)
    print (A)

if __name__ == "__main__": main()

"""YES. Improvement because number of comparisons are reduced. """
    