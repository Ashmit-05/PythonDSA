# Some error in deletion of a particular node
# See line no. 54
class Node :
    def __init__(self,val) :
        self.val = val 
        return


class CircularSingly :
    def __init__(self,val) :
        node = Node(val)
        node.next = node
        self.head = node
        self.tail = node
        self.len = 1
        return


    def insert(self,val,pos) :
        node = Node(val)
        if self.head == None :
            print("Please create the list first")
        else :
            if pos == 0 :
                node.next = self.head
                self.tail.next = node
                self.head = node
            elif pos >= self.len :
                self.tail.next = node
                node.next = self.head
                self.tail = node
            else :
                curr,i = self.head,0
                while i < pos-1 :
                    curr = curr.next
                    i += 1
                x = curr.next
                curr.next = node
                node.next = x
        self.len += 1
        return

    def search(self,val) :
        i = 0
        curr = self.head
        while i < self.len :
            if curr.val == val :
                return True
            if curr == self.tail :
                break
            curr = curr.next
        return False

    def delete(self,pos) :
        if self.head == None :
            print("The list is empty")
            return
        else :
            if pos == 0 :
                self.head = self.head.next
                self.tail = self.head
            elif pos >= self.len :
                curr,i = self.head,0
                while i < self.len-1 :
                    curr = curr.next
                    i += 1
                curr.next = self.head
                self.tail = curr
            else :
                curr,i = self.head,0
                while i < pos-1 :
                    curr = curr.next
                    i += 1
                curr.next = curr.next.next
            self.len -= 1 
            return


    def deleteList(self) :
        self.head = None
        self.tail = None
        return


    def printList(self) :
        if self.head == None :
            print("The list is empty")
            return
        i = 0
        curr = self.head
        while i < self.len :
            print(curr.val)
            if curr == self.tail :
                break
            curr = curr.next
        return

csll = CircularSingly(0)
csll.insert(1,0)
csll.insert(2,0)
csll.insert(17,17)
csll.insert(9,4)
csll.insert(3,1)
csll.printList()
print(csll.search(31))
print(csll.search(17))
csll.delete(0)
csll.printList()
csll.delete(3)
csll.printList()
csll.deleteList()
csll.printList()
