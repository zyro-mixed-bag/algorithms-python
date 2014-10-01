def insertionSort(A, size):
    for i in range(size):        
        temp = A[i]
        j = i-1
        while j>=0 and temp<A[j]: 
            j-=1

        del A[i]
        A.insert(j+1,temp)
    return A


def bucketSort(A, size):
    maximum = max(A) if max(A) != 0 else 1
    B = [[] for i in range(size)]
    
    for i in range(size):
        bucketNum = int((size-1)*(A[i]/maximum))
        B[bucketNum].append(A[i])
              
    for i in range(size):
        B[i] = insertionSort(B[i], len(B[i]))
        
    A = []
    for i in range(size):
        A.extend(B[i])
        
    return A

def main():
    A = [34, 24, 99, 23, 10, 54, 84,100, 0]
    A = bucketSort(A, len(A))
    print(A)

if __name__ == "__main__":main()
    