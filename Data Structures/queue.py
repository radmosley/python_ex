class Queue:
    def __init__(self, k):
        self.items = []
        self.size = k

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        self.items.pop()

    def shoeSize(self):
        return len(self.items)

    def showQueue(self):
        print(self.items)


que = Queue(10)
que.enqueue(1)
que.enqueue(2)
que.enqueue(3)
que.enqueue(4)
que.enqueue(6)
# print(que.size())
que.showQueue()
