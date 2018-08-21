class Deque():
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        return self.items.append(item)
    
    def addRear(self, item):
        return self.items.insert(0,item)

    def removeFront(self, item):
        return self.items.pop()

    def removeRear(self, item):
        return self.items.pop(0)

    def length(self):
        return len(self.items)

    def showDeque(self):
        print(self.items)


deque = Deque()
deque.addRear(4)
deque.addRear(5)
deque.addRear(7)
deque.addFront(1)
deque.addFront(2)
deque.addFront(3)
deque.removeRear(1)

deque.showDeque()
print(deque.length())