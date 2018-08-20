#Node Class

class Node:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

    def insert(self, data):
        if data < self.data:
            if not self.leftChild:
                self.leftChild = Node(data)
            else:
                self.leftChild.insert(data)
        else:
            if not self.rightChild:
                self.rightChild = Node(data)
            self.rightChild.insert(data)

    def removeNode(self, data, parentNode):
        if data < self.data:
            if self.leftChild is not None:
                self.leftChild.removeNode(data, self)

            elif data > self.data:
                if self.rightChild is not None:
                    self.rightChild.removeNode(data, self)

            else:
                if self.leftChild is not None and self.rightChild is not None:
                    self. data = self.rightChild.getMin()
                    self.rightChild.removeNode(self.data, self)
                elif parentNode.leftChild == self:
                    if self.leftChild is not None:
                        tempNode = self.leftChild
                    else:
                        tempNode = self.rightChild
                    
                    parentNode = self.rightChild
                elif parentNode.rightChild == self:
                    if self.leftChild is not None:
                        tempNode = self.leftChild
                    else:
                        tempNode = self.rightChild

                    parentNode.rightchild = tempNode

    def getMin(self):
        if self.leftChild is None:
            return self.data
        else:
            self.leftChild.getMin()

    def getMax(self):
        if self.rightChild is None:
            return self.data
        else:
            return self.rightChild.getMax()

    def traverseIndOrder(self):
        if self.leftChild is not None:
            self.leftChild.traverseIndOrder()
        print(self.data)

        if self.rightChild is not None:
            self.rightChild.traverseIndOrder()

#Binary Search Tree Class
class BST:
    def __init__(self):
        self.rootNode = None

    def insert(self, data):
        if not self.rootNode:
            self.rootNode = Node(data)
        else:
            self.rootNode.insert(data)

    def remove(self, dataToRemove):
        if self.rootNode:
            if self.rootNode.data == dataToRemove:
                tempNode = Node(None)
                tempNode.leftChild = self.rootNode
                self.rootNode.removeNode(dataToRemove, tempNode)
            else:
                self.rootNode.removeNode(dataToRemove, None)

    def getMax(self):
        if self.rootNode:
            return self.rootNode.getMax()

    def getMin(self):
        if self.rootNode:
            return self.rootNode.getMin()

    def traverseInOrder(self):
        if self.rootNode:
            self.rootNode.traverseIndOrder()


#Testing
bst = BST()

bst.insert(12)
bst.insert(10)
bst.insert(-3)
bst.insert(-2)

bst.traverseInOrder()
print(bst.getMin())