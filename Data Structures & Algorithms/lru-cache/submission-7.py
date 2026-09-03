class Node:
    def __init__(self, key):
        self.next=None
        self.prev=None
        self.key=key

class LRUCache:
    def __init__(self, capacity: int):
       self.keyValue = {}
       self.keyNode = {}
       self.LLStart = Node(-1)
       self.LLEnd = Node(-1)
       self.LLStart.next = self.LLEnd
       self.LLEnd.prev = self.LLStart

       self.capacity = capacity
       self.nodes=0

    def get(self, key: int) -> int:
        if key in self.keyValue:
            node = self.keyNode[key]
            node.prev.next = node.next
            node.next.prev = node.prev

            node.next = self.LLStart.next
            self.LLStart.next.prev = node
            node.prev = self.LLStart
            self.LLStart.next=node

            return self.keyValue[key]

        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.keyValue:
            node = self.keyNode[key]
            node.prev.next = node.next
            node.next.prev = node.prev

            node.next = self.LLStart.next
            self.LLStart.next.prev = node
            node.prev = self.LLStart
            self.LLStart.next=node

            self.keyValue[key] = value
        else:
            if self.capacity == self.nodes:
                toRemove = self.LLEnd.prev
                self.keyValue.pop(toRemove.key)
                toRemove.prev.next = self.LLEnd
                self.LLEnd.prev=toRemove.prev

                self.keyNode.pop(toRemove.key)
                self.nodes-=1
            
            newNode = Node(key)
            self.keyValue[key]=value
            self.keyNode[key]=newNode

            newNode.next = self.LLStart.next
            self.LLStart.next.prev = newNode
            newNode.prev = self.LLStart
            self.LLStart.next=newNode

            self.nodes+=1

            
        
       