class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def removeNode(self, data, previousNode):
        if self.data == data:
            previousNode.next == self.next
            del self.data
            del self.next
        else:
            if self.next != None:
                self.next.removeNode(data, self)

class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def traverseList(self):
        actualNode = self.head
        
        while actualNode != None:
            print('{}'.format(actualNode.data))
            actualNode = actualNode.next

    def insertStart(self, data):
        newNode = Node(data)
        self.length += 1

        if not self.head:
            self.head = newNode

        else:
            newNode.next = self.head
            self.head = newNode

    def size(self):
        return self.length

    def insertEnd(self, data):

        if self.head is None:
            self.insertStart(data)
            return

        self.length -= 1
        newNode = Node(data)
        actualNode = self.head

        while actualNode.next != None:
            actualNode = actualNode.next
        actualNode.next = newNode

    # def remove(self, data, previousNode):
    #     self.length -= 1
    #     if self.head:
    #         if data == self.head.data:
    #             self.head = self.head.next
    #         else:
    #             self.head.removeNode(data, self.head)


linkedList = LinkedList()
linkedList.insertEnd(12)
linkedList.insertEnd(122)
linkedList.insertStart(3)
linkedList.insertStart(36)
linkedList.traverseList()
# linkedList.remove(3)
linkedList.traverseList()

