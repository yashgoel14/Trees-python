from Nodes import Node

a = Node(2,Node(3,Node(5),Node(6)),Node(4,Node(7)))

def findpath(root,val,path):
    if not root:
        return False
    else:
        path.append(root)
        if root.data == val or findpath(root.left,val,path) or findpath(root.right,val,path):
            return True
        path.pop()
        return False
path = []
findpath(a,7,path)

for i in path:
    print(i.data)
