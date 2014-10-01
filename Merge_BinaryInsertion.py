#!/usr/bin/python3

def binarySearch(A, key, start, end):  
    if (start > end):
        return start
    else:
        mid =  int((start + end) / 2)
        if (A[mid] == key):
            return mid
        elif key < A[mid]:
            return binarySearch(A, key, start, mid-1)
        else:
            return binarySearch(A, key, mid+1, end)


# def binaryInsertionSort(A, size):
#     i = 1
#     while(i<size):
#         index = binarySearch(A, A[i], 0, i)
#         temp = A[i]
#         del A[i]
#         A.insert(index, temp)
#         i += 1          
#         """Shifting takes place internally .. No need to do-->
#         j = i-1
#         while(j >= index):
#             A[j+1] = A[j]
#             j+=1
#         A[index] = temp """    
#     return A


def binaryInsertionSort(A, size):
    i = 1
    
    while(i<size):
        index = binarySearch(A, A[i], 0, i)
        
        if(index < i):                                              ##Shift only if the new index comes before the current index
            temp = A[i]
            j = i-1
            
            while (j >= index):
                A[j+1] = A[j]
                j -= 1
                
            A[index] = temp    
        i += 1             
    return A


def mergeSort(A, threshold):
    if (len(A) <= 1):
        return A
     
    if (len(A) <= threshold):
        return binaryInsertionSort(A, len(A))
    else:
        mid = int(len(A) / 2)
        left = A[:mid]
        right = A[mid:]
        
        left = mergeSort(left, threshold)
        right = mergeSort(right, threshold)
        return (concatBuckets(left, right))
         
 
def concatBuckets(left, right):
    temp = list()
    i, j = 0, 0
     
    while(i < len(left) and j < len(right)):
        if(left[i] <= right[j]):
            temp.append(left[i])
            i += 1
        else:
            temp.append(right[j])
            j += 1
     
    if left:
        temp.extend(left[i:])
     
    if right:
        temp.extend(right[j:])
         
    return temp


def main():   
    A = [5,4,3,2,1]
    threshold = 0

    A = mergeSort(A, threshold)
    print (A)
    
if __name__ ==  "__main__" : main()