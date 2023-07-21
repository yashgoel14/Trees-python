from Nodes import Node
a = Node("a",Node("b",Node("d"),Node("e")),Node("c",Node("f"),Node("g")))
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data)
        inorder(root.right)
#inorder(a)

def preorder(root):
    if root:
        print(root.data)
        inorder(root.left)
        inorder(root.right)
#preorder(a)

def postorder(root):
    if root:
        inorder(root.left)
        inorder(root.right)
        print(root.data)
#postorder(a)
