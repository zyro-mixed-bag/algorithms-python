from math import log

def maxAbsVal(a):
    value = max(abs(num) for num in a)
    return value


def constructBuckets(base):
    buckets = [ [] for i in range(base) ]       #List of lists - Every bucket is a list#
    return buckets


def getBucketNum(number, base, currentPass):
    bucketNum = (number // (base ** currentPass) ) % base
    return bucketNum


def fillBuckets(a, base, currentPass):
    buckets = constructBuckets(base)
    for number in a:
        buckets[ getBucketNum(number, base , currentPass)].append(number)
    return buckets


def fillBucketsBySign(a):
    buckets = [ [], [] ]
    for num in a:
        if num<0:
            buckets[0].append(num)
        else:
            buckets[1].append(num)
    return buckets
    

def concatBuckets(buckets):
    newList = []
    for bucket in buckets:
        newList.extend(bucket)
    return newList

            
def radixSort(a, base):
    maximum = maxAbsVal(a)
    totalPasses = int (round(log(maximum, base)) + 1)
    
    newList = list(a)
    for currentPass in range(totalPasses):
        newList = concatBuckets(fillBuckets(newList, base, currentPass))
    
    newList = concatBuckets(fillBucketsBySign(newList))
    return newList


def main():
#     a = [int('1101',2), int('1100',2),int('0100',2),int('0101',2)]
#     a = radixSort(a, 2)
#     for num in a:
#         print(bin(num))

    a = [-2, 100, 199, 19, 1000, 0, 1]
    a = radixSort(a, 10)
    print(a) 
    
if __name__=="__main__":main()