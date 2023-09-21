import sys
sys.path.insert(0,'/home/keating/Desktop/Projects/PythonDSA/Queue')
from queue import Queue
from collections import deque

class TreeNode :
    def __init__(self,data) :
        self.data = data
        self.leftChild = None
        self.rightChild = None

# root node -> left node -> right node
def preOrder(rootNode) :
    if rootNode == None :
        return
    print(rootNode.data)
    preOrder(rootNode.leftChild)
    preOrder(rootNode.rightChild)

# left node -> root node -> right node
def inOrder(rootNode) :
    if rootNode == None :
        return
    inOrder(rootNode.leftChild)
    print(rootNode.data)
    inOrder(rootNode.rightChild)

# left node -> right node -> root node
def postOrder(rootNode) :
    if rootNode == None :
        return
    postOrder(rootNode.leftChild)
    postOrder(rootNode.rightChild)
    print(rootNode.data)

def levelOrder(rootNode) :
    if rootNode == None :
        return
    q = Queue()
    q.enqueue(rootNode)
    while q.isEmpty() == False :
        x = q.dequeue()
        print(x.data)
        if x.leftChild != None :
            q.enqueue(x.leftChild)
        if x.rightChild != None :
            q.enqueue(x.rightChild)

def search(rootNode,data) :
    if rootNode == None :
        print('Tree does not exist')
        return
    q = deque()
    q.append(rootNode)
    while len(q) != 0 :
        x = q.popleft()
        if x.data == data :
            print('Success')
            return
        if x.leftChild != None :
            q.append(x.leftChild)
        if x.rightChild != None :
            q.append(x.rightChild)
    print('Failure')

v = TreeNode('Vehicle')
t = TreeNode('two wheeler')
f = TreeNode('four wheeler')
c = TreeNode('car')
b = TreeNode('bus')
s = TreeNode('scooty')
bike = TreeNode('bike')
v.leftChild = t
v.rightChild = f
t.leftChild = s
t.rightChild = bike
f.leftChild = b
f.rightChild = c
# print('in order : ')
# inOrder(v)
# print('pre order : ')
# preOrder(v)
# print('post order : ')
# postOrder(v)
# print('level order : ')
# levelOrder(v)
print('searching : ')
search(v,'coffee')
search(v,'scooty')
