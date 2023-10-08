# Note that dfs can be implemented recursively but bfs is always iterative

from collections import deque

def depthFirst(graph, sourceNode) :
    stack = [sourceNode]
    while len(stack) > 0 :
        curr = stack.pop()
        print(curr)
        for neighbor in graph[curr] :
            stack.append(neighbor)

def breadthFirst(graph,sourceNode) :
    q = deque()
    q.appendleft(sourceNode)
    while len(q) > 0 :
        curr = q.pop()
        print(curr)
        for neighbor in graph[curr] :
            q.appendleft(neighbor)

# Using depth first search recursion
def hasPathdfs(graph,src,dst) :
    if src == dst :
        return True
    for neighbor in graph[src] :
        if hasPathdfs(graph,neighbor,dst) == True :
            return True

    return False

def hasPathbfs(graph,src,dst) :
    q = deque()
    q.appendleft(src)
    while len(q) > 0 :
        curr = q.pop()
        if curr == dst :
            return True
        for neighbor in graph[curr] : 
            q.appendleft(neighbor)
    return False

graph = {
        'a' : ['b','c'],
        'b' : ['d'],
        'c' : ['e'],
        'd' : ['f'],
        'e' : [],
        'f' : [],
        }

depthFirst(graph,'a')
breadthFirst(graph,'a')
print(hasPathdfs(graph,'a','d'))
print(hasPathdfs(graph,'a','z'))
print(hasPathbfs(graph,'a','d'))
print(hasPathbfs(graph,'a','z'))
