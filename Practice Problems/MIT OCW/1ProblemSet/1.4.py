# see reorder function
# problem 1.4 : jen & berry's
class Node:
    def __init__(self,val,next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self,node):
        self.head = node
    @property
    def size(self):
        curr = self.head
        size = 0
        while curr != None:
            size += 1
            curr = curr.next
        return size

    def __len__(self):
        curr = self.head
        size = 0
        while curr != None:
            size += 1
            curr = curr.next
        return size


    def print_list(self):
        curr = self.head
        while curr != None:
            print(curr.val)
            curr = curr.next

    def reverse(self):
        prev = None
        curr = self.head
        while curr is not None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        self.head = prev

    def reorder(self): # problem 1.4
        n = len(self)//2
        a = self.head
        for _ in range(n - 1):
            a = a.next
        b = a.next
        x_p,x = a,b
        for _ in range(n):
            x_n = x.next
            x.next = x_p
            x_p,x = x,x_n
        a.next = x_p
        b.next = None



n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
l = LinkedList(n1)
# print(l.size)
# print(len(l))
print("before")
l.print_list()
l.reorder()
print("after")
l.print_list()
