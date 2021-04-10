class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = Node()
        
    def append(self, data):
        new_node = Node(data)
        curNode = self.head
        
        while curNode.next != None:
            curNode = curNode.next
        curNode.next = new_node
    
    def display(self):
        items = []
        curNode = self.head 
        while curNode.next != None:
            curNode = curNode.next
            items.append(curNode.data)
        print(items)
        
    def length(self):
        
        curNode = self.head
        total = 0
        
        while curNode.next != None:
            curNode = curNode.next
            total += 1
        return total
        
    def get(self, index):
        if index > self.length():
            print("Error, out of bounds")
            return None
        indexOfNode = 0
        curNode = self.head
        
        while curNode.next != None:
            curNode = curNode.next
            if indexOfNode == index:return curNode.data
            indexOfNode += 1
        
    def erase(self, index):
        if index >= self.length():
            print("Error, out of bounds")
            return 
        indexOfNode = 0
        curNode = self.head
        
        while True:
            lastNode = curNode
            curNode = curNode.next
            if indexOfNode == index:
                lastNode.next = curNode.next
                return
            indexOfNode += 1
        
        
        
myLinkedList = LinkedList()

myLinkedList.append(2)
myLinkedList.append(4)
myLinkedList.append(8)
myLinkedList.append(16)
myLinkedList.append(32)
myLinkedList.append(64)
myLinkedList.append(128)
myLinkedList.append(256)
myLinkedList.display()
myLinkedList.erase(6)
myLinkedList.display()
