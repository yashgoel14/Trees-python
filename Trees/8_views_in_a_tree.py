from Nodes import Node
from collections import deque

a = Node(2,Node(3,Node(5),Node(6)),Node(4,Node(7)))

def leftviewutil(root,d,level):
    if not root:
        return
    else:
        if level not in d:
            d[level] = root.data
    leftviewutil(root.left,d,level+1)
    leftviewutil(root.right,d,level+1)

def rightviewutil(root,d,level):
    if not root:
        return
    else:
        d[level] = root.data
    
    leftviewutil(root.left,d,level+1)
    leftviewutil(root.right,d,level+1)
    
    
def leftviewBT(root):
    d = {}
    leftviewutil(root,d,0)
    print(d)
#leftviewBT(a)

def rightviewBT(root):
    d = {}
    rightviewutil(root,d,0)
    print(d)
#rightviewBT(a)


d = {}
def topviewBT(root):
    queue = [(root,0)]
    while queue:
        u = queue.pop()
        if u[1] not in d:
            d[u[1]] = u[0].data
        if u[0].left:
            queue.append((u[0].left,u[1]-1))
        if u[0].right:
            queue.append((u[0].right,u[1]+1))

def bottomviewBT(root):
    queue = [(root,0)]
    while queue:
        u = queue.pop()
        d[u[1]] = u[0].data
        if u[0].left:
            queue.append((u[0].left,u[1]-1))
        if u[0].right:
            queue.append((u[0].right,u[1]+1))

#topviewBT(a)
bottomviewBT(a)
print(d)
    
