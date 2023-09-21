class Stack :
    def __init__(self) :
        self.list = []

    def printStack(self) :
        for i in self.list :
            print(i)
        return

    def push(self,val) :
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

s = Stack()
print(s.isEmpty())
s.push(1)
s.push(2)
s.push(3)
s.push(5)
s.push(4)
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

