class Stack :
    def __init__(self,maxSize) :
        self.list = []
        self.maxSize = maxSize

    def printStack(self) :
        for i in self.list :
            print(i)
        return

    def push(self,val) :
        if self.isFull() :
            print("the stack is full")
            return
        self.list.append(val)
        return

    def pop(self) :
        return self.list.pop()
    
    def peek(self) :
        print(self.list[-1])
        return

    def isEmpty(self) :
        if len(self.list) == 0 :
            return True
        return False

    def isFull(self) :
        if len(self.list) == self.maxSize :
            return True
        return False

s = Stack(5)
print(s.isEmpty())
print(s.isFull())
s.push(1)
s.push(2)
s.push(3)
s.push(5)
s.push(4)
print(s.isFull())
s.push(6)
print("top element : ")
s.peek()
print("this is the current stack : ")
s.printStack()
print("popped elements : ")
print(s.pop())
print(s.pop())
print("new stack : ")
s.printStack()
print("top element : ")
s.peek()
print(s.isEmpty())

