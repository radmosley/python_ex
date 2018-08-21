class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next =newnext

class linkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def addNode(self, item):
        node = Node(item)
        node.setNext(self.head)
        self.head = node

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()
        print(count)

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if  current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    def show(self):
        clist = []
        current = self.head
        while current != None:
            clist.append(current.data)
            current = current.next
        print(clist)

linkedlist = linkedList()
linkedlist.addNode(1)
linkedlist.addNode(2)
linkedlist.addNode(3)
linkedlist.addNode(5)
print(linkedlist.isEmpty())
linkedlist.size()
linkedlist.remove(3)
linkedlist.show()
print(linkedlist.search(3))