def binaryTree(r):
    rootNode = [r,[],[]]
    return rootNode

def insertLeft(rootNode, newNode):
    t = rootNode.pop(1)
    if len(rootNode) > 1:
        rootNode.insert(1, [newNode, t, [] ])
    else:
        rootNode.insert(1, [ newNode, [], [] ])
    return rootNode

def insertRight(rootNode, newNode):
    t = rootNode.pop(2)
    if len(t) > 1:
        rootNode.insert(2, [newNode, [], t ])
    else:
        rootNode.insert(2, [newNode, [], [] ])
    return rootNode

def getRootValue(root):
    return root[0]

def setRootData(root, data):
    root[0] = data
    return root

def getLeftChild(root):
    return root[1]

def getRightChild(root):
    return root[2]

tree = binaryTree(0)
insertLeft(tree, 1)
insertRight(tree, 2)
insertLeft(tree, 3)
insertRight(tree, 4)
insertLeft(tree, 5)
insertRight(tree, 6)
insertLeft(tree, 7)
insertRight(tree, 8)
print(getRootValue(tree))
setRootData(tree, 111)
print(getRootValue(tree))
print(getLeftChild(tree))
print(getRightChild(tree))
print(tree)