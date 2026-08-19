class Node:
    def __init__(self, key):
        self.next=None
        self.prev=None
        self.key=key

class LRUCache:
    def __init__(self, capacity: int):
        self.mainMap = {}
        self.head = Node(-1)
        self.tail=Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head

        self.mapUsed=0
        self.capacity = capacity
        self.keyMap ={}

    def get(self, key: int) -> int:
        if key in self.mainMap:
            node = self.keyMap[key]
            node.prev.next = node.next
            node.next.prev = node.prev
            self.tail.prev.next=node
            node.next = self.tail
            node.prev = self.tail.prev
            self.tail.prev = node

            curr = self.head
            
            return self.mainMap[key]

        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.mainMap:
            node = self.keyMap[key]
            node.prev.next = node.next
            node.next.prev = node.prev
            self.tail.prev.next=node
            node.next = self.tail
            node.prev = self.tail.prev
            self.tail.prev = node

            curr = self.head
        else:
            if self.mapUsed == self.capacity:
                toRemove = self.head.next
                self.head.next = toRemove.next
                toRemove.next.prev = self.head

                self.keyMap.pop(toRemove.key)
                self.mainMap.pop(toRemove.key)
            else:
                self.mapUsed+=1
            
            newNode = Node(key)
            self.tail.prev.next=newNode
            newNode.next = self.tail
            newNode.prev = self.tail.prev
            self.tail.prev = newNode
            self.keyMap[key] = newNode

        self.mainMap[key]=value

        
       