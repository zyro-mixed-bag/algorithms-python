def insert(T, key, size):
	for i in range(size):
		j = hashLinearProbe(key, i, size)
		if T[j] is None or T[j] is -1:
			T[j] = key
			return T
		else:
			i += 1
	print("Table full -- Rehashing")
	T = rehashTable(T, size)
	insert(T, key, size)
	return T

def search(T, key, size):
	i = 0
	while i < size or T[i] is None:
		j = hashLinearProbe(key, i , size)
		if T[j] == key:
			return j
		else:
			i += 1
	return None

def delete(T, key, size):
	j = search(T, key, size)
	if j is not None:
		T[j] = -1

def hashFunDivisionMethod(key, size):
		return key % size

"""mid-square method
{	
	// 9452 * 9452 = 89 3403 04 : address is 3403
	x = 9452
	//select the middle four digits .. //APPEND ZEROES TO MAKE 8-digits
	print((x * x//100)%10000)
        //select the middle six digits
        address = (x * x // 100) % 1000000;
}
"""

"""Folding
There are two folding methods that are used, fold shift and fold boundary. In fold shift, 
the key value is divided into parts whose size matches the size of the required address. 
Then the left and right parts are shifted and added with the middle part.

In fold boundary, the left and right numbers are folded on a fixed boundary between 
them and the center number.

a. Fold Shift

Key:	123456789

	123
	456
	789
	---
       1368 ( 1 is discarded)

b. Fold Boundary

Key:	123456789

	321 (digit reversed)
	456
	987 (digit reversed)
	---
       1764 ( 1 is discarded)
       """
	
def hashLinearProbe(key, i, size):
	return ((hashFunDivisionMethod(key, size) + i) % size)

def hashQuadProbe(key, i, size, c1, c2):
	return ((hashFunDivisionMethod(key, size) + c1 * i + c2 * i * i) % size)

def hashDoubleHashing(key, i, size):
	return((hashFunDivisionMethod(key, size) + i * hashFunDivisionMethod(key, size)) % size)

def rehashTable(T, size):
	newSize = size * 2
	temp = [None for i in range(newSize)]
	for element in T:
		insert(temp, element, newSize)
	T = temp
	return T
		
def main():
	size = 10
	T = [None for i in range(size)]
	insert(T, 5, size)
	print(T)
	insert(T,3,size)
	print(T)
	insert(T,15,size)
	print(T)
	insert(T,1,size)
	print(T)
	insert(T,1,size)
	print(T)
	insert(T,10,size)
	print(T)
	insert(T,11,size)
	print(T)
	insert(T,6,size)
	print(T)
	insert(T,9,size)
	print(T)
	insert(T,9,size)
	print(T)
	T = insert(T,14,size)
	print(T)
if __name__=='__main__':main()
	
