#!/usr/bin/python
import math

class ListNode:
    def __init__(self, data, next, previous):
        self.data = data
        self.next = next
        self.previous = previous


class List:
    def __init__(self):
        self.head = None
        self.tail = None
    
        
    def insertBeginning(self, data):
        newNode = ListNode(data, self.head, None)
        if self.head is not None:
            self.head.previous = newNode
            self.head = newNode
        else:
            self.head = self.tail = newNode
    
        
    def insertEnd(self, data):
        newNode = ListNode(data, None, self.tail)
        if self.tail is not None:
            self.tail.next = newNode
            self.tail = newNode
        else:
            self.head= self.tail= newNode
        
            
    def insertIndex(self, position, data):
        newNode = ListNode(data, None, None)
        temp = self.head
        
        if temp is None or position is 0:
            self.insertBeginning(data)
            return
            
        i=0
        while(i<position-1 and temp.next is not None):
            temp = temp.next
            i += 1

        if temp.next is None:
            self.insertEnd(data)     
        else:
            newNode.next = temp.next
            temp.next = newNode
            temp.next.previous = temp
            newNode.next.previous = newNode
        
                     
    def deleteBeginning(self):
        if self.head is None:
            self.tail = None
            return
        
        if self.head.next is None:
            self.head = self.tail = None
            return
        
        self.head.next.previous = None
        self.head = self.head.next
         
            
    def deleteEnd(self):
        if self.tail is None:
            self.head = None
            return
        
        if self.head.next is None:
            self.head = self.tail = None
            return
        
        self.tail.previous.next = None
        self.tail = self.tail.previous
        
        
    def deleteIndex(self,position):
        temp = self.head
        
        if temp is None or position < 0:
            return
        
        if position is 0:
            self.deleteBeginning()
            return
        
        i=0
        while(i<position-1 and temp.next is not None):
            temp = temp.next
            i += 1
            
        if temp.next is None:
            self.deleteEnd()
        else:
            temp.next.previous = None
            temp.next = temp.next.next
            if temp.next is not None:
                temp.next.previous = temp
     
            
    def printList(self):
        node = self.head
        while node is not None:
            print(node.data)
            node = node.next
            
    def nodeCount(self):
        node = self.head
        count = 0
        while node is not None:
            count += 1
            node = node.next
        return count 
            
            
    def selectionSort(self):
        if self.head is None:
            return
        
        first = self.head
        while first.next is not None:
            minNode = first
            second = first.next
            while second is not None:
                if second.data < minNode.data:
                    minNode = second
                second = second.next
                    
            if minNode is not first:
                first.data, minNode.data = minNode.data, first.data
            first = first.next
            
            
    def binarySearch(self, mid, key, low, high):
        if self.head is None or low.data >= high.data:
            return -1
        
        midNode = low
        count = 1
        while count < mid:
            midNode = midNode.next
            count += 1
            
        if (midNode.data == key):
            return mid
        
        elif (key< midNode.data):
            return self.binarySearch(math.ceil(mid/2), key, self.head, midNode.previous)
            
        else:
            return mid + self.binarySearch(math.ceil(mid/2), key, midNode.next, self.tail)
            
        return -1
              
        
             
                    
myList = List()
myList.insertBeginning(12)
myList.insertBeginning(1)
myList.insertBeginning(2)
myList.insertBeginning(13)
myList.insertBeginning(16)
myList.insertBeginning(23)

myList.selectionSort()
myList.printList()
mid = math.ceil(myList.nodeCount() / 2)
key = 3

position = myList.binarySearch(mid, key, myList.head, myList.tail)
if(position == -1):
    print("\nNot Found")
else:
    print("Position is ", position)

