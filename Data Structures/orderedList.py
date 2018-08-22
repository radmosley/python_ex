class Node:
    def __init__(self):
        pass

class OrderedList:
    def __init__(self):
        self.head = None

    def add(self, item):
        pass
    def remove(self, item):
        pass
    def search(self, item):
        current = self.head
        found = False
        stop = False
        while current != None and not found and not stop:
            if current.getData() == item:
                found = True
            else:
                if current.getData() > item:
                    stop = True
                else:
                    current = current.getNext()
        return found
        
    def isEmpty(self):
        pass

    def size(self):
        pass
        
    def index(self, item):
        pass

    def pop(self):
        pass
        
    def pop2(self, pos):
        pass