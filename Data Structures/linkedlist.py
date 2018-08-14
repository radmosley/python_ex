class Node:
    def __init__(self, name):
        self.name = name
        self.next = None
    
    def __str__(self):
        return str(self.name)

class LinkedList:
    def __init__(self):
        self.head = None

    def listprint(self):
        printname = self.head
        while printname is not None:
            print(printname.name)
            printname = printname.next
    
    def insertBeginning(self, newdata):
        NewNode = Node(newdata)
        NewNode.next = self.head
        self.head = NewNode

list1 = LinkedList()
list1.head = Node('node1')
n2 = Node('node2')
n3 = Node('node3')
n4 = Node('node4')
n5 = Node('node5')
n6 = Node('node6')

list1.head.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6

list1.insertBeginning("node0")
list1.listprint()




