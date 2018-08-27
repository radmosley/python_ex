class MyCircularQueue:
    def __init__(self, k):
        self.size = k
        self.items = []
        
    def Front(self):
        if self.items == []:
            return -1
        return self.items[0]
    
    def Rear(self):
        if self.items == []:
            return -1
        return self.items[len(self.items)-1]
    
    def enQueue(self, value):
        self.items.insert(len(self.items), value)
    
    def deQueue(self):
        self.items.pop(0)
    
    def isEmpty(self):
        return self.items == []
    
    def isFull(self):
        if len(self.items) == self.size:
            return True

alist = MyCircularQueue(10)
alist.enQueue(1)
alist.enQueue(2)
alist.enQueue(3)
alist.enQueue(4)
alist.enQueue(6)
alist.deQueue()
print(alist.Front())