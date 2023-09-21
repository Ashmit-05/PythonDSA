class Node :
    def __init__(self,val) :
        self.val = val

class SinglyLinkedList :
    def __init__(self) :
        self.head = None
        self.tail = None
        self.len = 0


    def insert(self,val,pos) :
        node = Node(val)
        if(self.len == 0) :
            self.head = node
            self.tail = node
        else:
            if(pos == 0) :
                node.next = self.head
                self.head = node
            elif(pos >= self.len) :
                node.next = None
                self.tail.next = node
                self.tail = node
            else :
                i = 0
                curr = self.head
                while(i < pos-1) :
                    curr = curr.next
                    i += 1
                n = curr.next
                curr.next = node
                node.next = n
        self.len += 1

    def search(self,val) :
        curr = self.head
        while curr is not None :
            if curr.val is val :
                return True
            curr = curr.next
        return False

    def deleteNode(self,pos) :
        if self.head is None :
            print("The list is empty")
        else :
            if pos == 0 :
                self.head = self.head.next
            elif pos >= self.len :
                curr = self.head
                while (curr.next != self.tail) :
                    curr = curr.next
                curr.next = None
                self.tail = curr
            else :
                curr = self.head
                i = 0
                while i < pos-1 :
                    curr = curr.next
                    i += 1
                n = curr.next.next
                curr.next = n
        self.len -= 1

    def deleteList(self) :
        self.head = None
        self.tail = None


    def printList(self) :
        if self.head is None :
            print("The list is empty")
        curr = self.head
        while(curr is not None) :
            print(curr.val)
            curr = curr.next


sll = SinglyLinkedList()
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
sll.insert(1,1)
sll.insert(2,1)
sll.insert(3,1)
sll.insert(4,1)
sll.insert(0,0)
sll.insert(0,4)
print(sll.search(0))
print(sll.search(7))
sll.printList()
sll.deleteNode(0)
sll.deleteNode(17)
sll.deleteNode(2)
sll.printList()
sll.deleteList()
sll.printList()
