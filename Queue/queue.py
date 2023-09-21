class Queue :
    def __init__(self) :
        self.list = []

    def isEmpty(self) :
        if len(self.list) == 0 :
            return True
        return False

    def enqueue(self,val) :
        self.list.insert(0,val)

    def dequeue(self) :
        return self.list.pop()

    def printQueue(self) :
        print(self.list)

    def peek(self) :
        return self.list[-1]

    def delete(self) :
        self.list = []

q = Queue()
print(q.isEmpty())
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
q.printQueue()
print(q.isEmpty())
print(q.dequeue())
print(q.dequeue())


