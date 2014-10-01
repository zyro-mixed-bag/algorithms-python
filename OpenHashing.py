class myNode:
		def __init__(self, next=None, value=None):
				self.value = value
				self.next = next

def search(T, key, size):
		index = hashFunDivisionMethod(key, size)
		head = T[index]
		while head is not None:
				if head.value == key:
						return index
				else:
						head = head.next
		return None

def insert(T, key, size):
		index = hashFunDivisionMethod(key, size)
		if T[index].value is None:
				T[index].value = key
		else:
				head = T[index]
				while head.next:
						head = head.next
				temp = myNode(None, key)
				head.next = temp
				
def delete(T, key, size):
		index = hashFunDivisionMethod(key, size)
		
		head = T[index]
		if head.value == key:
				temp = head
				head = head.next
				T[index] = head
				del temp
		else:
				while head.next.value != key:
						head = head.next
				temp = head.next
				head.next = head.next.next
				del temp
						
def hashFunDivisionMethod(key, size):
		return key % size
				
def main():
		size = 10
		T = [myNode() for i in range(size)]
		insert(T, 5, size)
		insert(T, 15, size)
		print(search(T, 5,size))

if __name__ == "__main__":main()