class nodeObj:
	def __init__(self, value, left=None, right=None, parent=None):
		self.value = value
		self.left = left
		self.right = right
		self.parent = parent
		self.height = 0
		
def insertNode(root, node):
	if root is None:
		root = node
	
	elif node.value < root.value:
		if root.left is None:
			node.height += 1
			root.left = node
			root.left.parent = root
			maintainAVL(node.parent)
		else:
			node.height += 1
			insertNode(root.left, node)
			
	else:
		if root.right is None:
			node.height += 1
			root.right = node
			root.right.parent = root
			maintainAVL(node.parent)
		else:
			node.height += 1
			insertNode(root.right, node)
	
	while root.parent is not None:
		root = root.parent
	return root
		
def inOrderPrint(root):
	if root is None:
		return
	inOrderPrint(root.left)
	print(root.value)
	inOrderPrint(root.right)
	
def preOrderPrint(root):
	if root is None:
		return
	print(root.value)
	preOrderPrint(root.left)
	preOrderPrint(root.right)
	
def postOrderPrint(root):
	if root is None:
		return
	postOrderPrint(root.left)
	postOrderPrint(root.right)
	print(root.value)

def breadthFirstPrint(root):
	thisLevel = [root]
	while len(thisLevel) != 0:
		nextLevel = []
		for node in thisLevel:
			print (node.value)
			if node.left is not None: nextLevel.append(node.left)
			if node.right is not None: nextLevel.append(node.right)
		print("New Level")
		thisLevel = nextLevel
		
def searchNode(root, key):
	if root is None or root.value == key:
		return root
	else:
		if key < root.value:
			return searchNode(root.left, key)
		else:
			return searchNode(root.right, key)

def minNode(root):
	if root.left is not None:
		return minNode(root.left)
	else:
		return root
	
def maxNode(root):
	if root.right is not None:
		return maxNode(root.right)
	else:
		return root

def sortList(A, root):
	A = inOrderSort(root, [])
	return A

def inOrderSort(root, A):
	if root is None:
		return A
	A = inOrderSort(root.left, A)
	A.append(root.value)
	return inOrderSort(root.right, A)

def findSuccessor(root, node):
	if node.right is not None:
		return minNode(node.right)
	
	successor = None
	while root is not None:
		if node.value < root.value:
			successor = root
			root = root.left
		elif node.value > root.value:
			root = root.right
		else:
			break
	return successor
			
def findPredecessor(root, node):
	if node.left is not None:
		return maxNode(node.left)
	
	predecessor = None
	while root is not None:
		if node.value > root.value:
			predecessor = root
			root = root.right
		elif node.value < root.value:
			root = root.left
		else:
			break
	return predecessor

def deleteNode(node, parent, root):
		temp = node.parent
		# 0 children
		if node.left is None and node.right is None:
			if parent is not None:
				if parent.left is node:
					parent.left = None
				else:
					parent.right = None
			if parent is None:
				return parent
			
			del node
			while temp: 
				maintainAVL(temp)
				root =temp
				temp = temp.parent					
			
			return root
			
		# 1 child
		elif node.left is None or node.right is None:
			if node.left:
				n = node.left
			else:
				n = node.right
				
			if parent:
				if parent.left is node:
					parent.left = n
				else:
					parent.right = n
				
			del node
			while temp: 
				maintainAVL(temp)
				n = temp
				temp = temp.parent					

			return n
			
		# 2 children
		else:
			parent = node
			succ = node.right
			while succ.left:
				parent = succ
				succ = succ.left	   
			node.value = succ.value
			if parent.left == succ:
				parent.left = succ.right
			else:
				parent.right = succ.right
			
			while temp: 
				maintainAVL(temp)
				root = temp
				temp = temp.parent		
			return root

def deepestChild(node):
	leftDeep = rightDeep = node
	if node.left:
		leftDeep = deepestChild(node.left)
	if node.right:
		rightDeep = deepestChild(node.right)
	return leftDeep if leftDeep.height >= rightDeep.height else rightDeep
				
def checkBalance(node):
	if node is None:
		return 0
	
	if node.left:
		leftBalance = (deepestChild(node.left)).height - node.height
	else:
		leftBalance = 0
		
	if node.right:
		rightBalance = (deepestChild(node.right)).height - node.height
	else:
		rightBalance = 0
		
	if abs(leftBalance - rightBalance) <= 1:
		return 0							#Balanced
	elif leftBalance > rightBalance:
		return -1						#Left Unbalance
	else:
		return 1							#Right Unbalance

def checkHeavy(node):
	if node is None:
		return 0
	
	if node.left:
		leftBalance = (deepestChild(node.left)).height - node.height
	else:
		leftBalance = 0
		
	if node.right:
		rightBalance = (deepestChild(node.right)).height - node.height
	else:
		rightBalance = 0
	if leftBalance - rightBalance == 1:
		return -1						#Left Heavy
	elif  leftBalance - rightBalance == -1:
		return 1							#Right Heavy
	else:
		return 0							#Equal Heavy

def changeHeight(node, factor):
	if node.left:
		node.left.height += factor
		changeHeight(node.left, factor)
		
	if node.right:
		node.right.height += factor
		changeHeight(node.right, factor)
	
def singleRight(A):
	tempParent = A.parent
	B = A.left
	
	T = None
	if B:
		T = B.right
		B.parent = tempParent
		B.right = A
		B.height -= 1
		if B.left:
			B.left.height -= 1
			changeHeight(B.left, -1)
			
	if tempParent:
		if tempParent.left is A:
			tempParent.left = B
		else:
			tempParent.right = B

	A.left = T
	A.parent = B
	A.height += 1
	
	if A.right:
		A.right.height += 1
		changeHeight(A.right, 1)
	if T:
		T.parent = A
	
	return B

def singleLeft(A):
	tempParent = A.parent
	B = A.right
	
	T = None
	if B:
		T = B.left
		B.parent = tempParent
		B.left = A
		B.height -= 1
	
		if B.right:
			B.right.height -= 1
			changeHeight(B.right, -1)
		
	if tempParent:
		if tempParent.left is A:
			tempParent.left = B
		else:
			tempParent.right = B
	
	A.right = T
	A.parent = B
	A.height += 1
	
	if A.left:
		A.left.height += 1
		changeHeight(A.left, 1)
	if T:
		T.parent = A
		
	return B

def doubleRight(A):
	C = A.right
	B = singleRight(C)
	B = singleLeft(A)
	return B 
	
def doubleLeft(A):
	C = A.left
	B = singleLeft(C)
	B = singleRight(A)
	return B 

def maintainAVL(node):
	if node is None:
		return None
	flagBalance = checkBalance(node)
	
	if flagBalance == 0:
		if node.parent is None:
			return node
		else:
			node = maintainAVL(node.parent)
	elif flagBalance == -1:
		flagHeavy = checkHeavy(node.left)
		if flagHeavy == -1 or flagHeavy == 0:
			node = singleRight(node)
		else:
			node = doubleLeft(node)
	else:
		flagHeavy = checkHeavy(node.right)
		if flagHeavy == 1 or flagHeavy == 0:
			node = singleLeft(node)
		else:
			node = doubleRight(node)	
	return node
		
				
def main():
	A = [3, 2, 1, 4, 5, 6, 7, 16, 15, 14, 13, 12, 11, 10, 8, 9]
	#A = [20,10, 35, 5, 15, 25, 40, 18, 30, 38, 45, 50]
	
	root = None
	for value in A:
		root = insertNode(root, nodeObj(value))
	#inOrderPrint(root)	
	breadthFirstPrint(root)
	
# 	print("--------------")
# 	node = searchNode(root, 5)
# 	root = deleteNode(node, node.parent, root)
# 	breadthFirstPrint(root)


if __name__ == '__main__':main()		
