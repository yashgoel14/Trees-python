from Nodes import Node

a = Node(20,Node(15,Node(14,None,Node(17)),Node(18,Node(16),Node(19))),Node(40,Node(30),Node(60,Node(50))))

msum = 0
def f(root):
    if not root:
        return 10**5,-10**5,0
    lmin,lmax,lsum = f(root.left)
    rmin,rmax,rsum = f(root.right)

    if lmax<root.val and root.val<rmin:
        global msum
        msum = max(msum,lsum+1+rsum)
        return min(lmin,root.val),max(rmax,root.val),lsum+rsum+1
    return -10**5,10**5,0
        
def max_bst_bt(root):
    f(root)
    return msum
print(max_bst_bt(a))
