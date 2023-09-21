class Node :
    def __init__(self,val = None) :
        self.val = val

class LinkedList :
    def __init__(self) :
        self.head = None

class Stack :
    def __init__(self) :
        self.list = LinkedList()

    def push(self,val) :
        node = Node(val)
        node.next = self.list.head
        self.list.head = node

    def pop(self) :
        x = self.list.head.val
        self.list.head = self.list.head.next
        return x

    def peek(self) :
        print(self.list.head.val)

    def isEmpty(self) :
        return self.list.head == None

    def printStack(self) :
        curr = self.list.head
        while curr != None :
            print(curr.val)
            curr = curr.next

s = Stack()
print(s.isEmpty())
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)
print("full stack :")
s.printStack()
print("top element : ")
s.peek()
print("popped elements : ")
print(s.pop())
print(s.pop())
print('full stack : ')
s.printStack()
