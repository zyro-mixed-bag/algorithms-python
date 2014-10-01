class nodeObj:
    def __init__(self,value, left = None, right = None, parent = None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

def buildBST(A):
    root = nodeObj(A[0])
    for element in A[1:]:
        root = insertNode(root, nodeObj(element))
    return root
        
def insertNode(root, node):
    if root is None:
        root = node
    
    elif node.value < root.value:
        if root.left is None:
            root.left = node
            root.left.parent = root
        else:
            insertNode(root.left, node)
            
    else:
        if root.right is None:
            root.right = node
            root.right.parent = root
        else:
            insertNode(root.right, node)
            
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

def sortList(A):
    root = buildBST(A)
    A = inOrderSort(root, [])
    return A

def inOrderSort(root,A):
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
                root = temp
                temp = temp.parent        
            return root
        
        
def main():
    A = [12,6,20,3,8,15,22,1,4,7,9,13,16,21,23]
    root = buildBST(A)
    node = searchNode(root, 20)
    deleteNode(node, node.parent, root)
    breadthFirstPrint(root)

if __name__ == '__main__':main()        