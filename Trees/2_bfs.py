from Nodes import Node
from collections import deque

a = Node("a",Node("b",Node("d"),Node("e")),Node("c",Node("f"),Node("g")))

def levelorder1(root):
    q = deque([root])
    while q:
        x = q.pop()
        print(x.data)

        if x.left:
            q.appendleft(x.left)
        if x.right:
            q.appendleft(x.right)
#levelorder1(a)

def levelorder2(root):
    q = deque([None,root])
    while True:
        x = q.pop()
        if x: # if element
            print(x.data)
            if x.left:
                q.appendleft(x.left)
            if x.right:
                q.appendleft(x.right)
        else: # if dummy node
            print("----")
            #to prevent infinite loop
            if len(q):
                q.appendleft(None)
            else:  
                break
#levelorder2(a)

ans = []
def levelorder3(root):
    q = deque([None,root])
    while True:
        l = []
        x = q.pop()
        if x:
            l.append(x.data)
            if x.left:
                q.appendleft(x.left)
            if x.right:
                q.appendleft(x.right)
        else:
            ans.append(l)
            if len(q):
                q.appendleft(None)
            else:
                break
    return ans
#print(levelorder3(a))

def levelorder4(root):
    queue = [root]
    next_queue = []
    level = []
    result = []
    while queue:
        for u in queue:
            level.append(u.data)
            if u.left:
                next_queue.append(u.left)
            if u.right:
                next_queue.append(u.right)
            
        result.append(level)
        queue = next_queue
        next_queue = []
        level = []
    return result
#print(levelorder4(a))
