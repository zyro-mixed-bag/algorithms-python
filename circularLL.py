#!/usr/bin/python
import math

class ListNode:
    def __init__(self, data, next):
        self.data = data
        self.next = next



class List:
    def __init__(self):
        self.head = None
        self.tail = None
    
        
    def insertBeginning(self, data):
        newNode = ListNode(data, self.head)
        if self.head is not None:
            self.head = newNode
            self.tail.next = self.head         
        else:
            self.head = self.tail = newNode
    
        
    def insertEnd(self, data):
        newNode = ListNode(data, self.head)
        if self.tail is not None:
            self.tail.next = newNode
            self.tail = newNode
        else:
            self.head= self.tail= newNode
        
            
    def insertIndex(self, position, data):
        newNode = ListNode(data, None)
        temp = self.head
        
        if temp.next is None or position is 0:
            self.insertBeginning(data)
            return
            
        i=0
        while(i<position-1 and temp.next is not self.head):
            temp = temp.next
            i += 1

        if temp.next is self.head:
            self.insertEnd(data) 
        else:
            newNode.next = temp.next
            temp.next = newNode
        
                     
    def deleteBeginning(self):
        if self.head is None:
            self.tail = None
            return
        
        if self.head.next is self.head:
            self.head = self.tail = None
            return
        
        self.tail.next =self.head.next 
        self.head = self.tail.next
         "FROM HERE-------------------"
            
    def deleteEnd(self):
        if self.tail is None:
            self.head = None
            return
        
        if self.head.next is self.head:
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
                    
                    
myList = List()
myList.insertBeginning(12)
myList.insertBeginning(1)
myList.insertBeginning(2)
myList.insertBeginning(13)
myList.insertBeginning(16)
myList.selectionSort()
myList.printList()