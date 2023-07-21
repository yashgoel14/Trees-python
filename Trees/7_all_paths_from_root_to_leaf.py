from Nodes import Node

a = Node(2,Node(3,Node(5),Node(6)),Node(4,Node(7)))

ans = []
def allpaths(root,l):
    global ans
    if not root:
        return
    else:
        l.append(root.data)

        if not root.left and not root.right:
            ans.append(int("".join(map(str,l))))
            #ans.append("".join(l))   #in case of tree having alphabets
            
        allpaths(root.left,l)
        allpaths(root.right,l)
        l.pop()
        
l=[]
#allpaths(a,l)
#print(ans)

def allpaths2(root,l,ans):
    if not root:
        return
    else:
        l.append(root.data)

        if not root.left and not root.right:
            ans.append(int("".join(map(str,l))))
            #ans.append("".join(l))   #in case of tree having alphabets
            
        allpaths2(root.left,l,ans)
        allpaths2(root.right,l,ans)
        l.pop()
        
allpaths2(a,l,ans)

