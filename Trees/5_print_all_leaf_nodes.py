from Nodes import Node

a = Node(2,Node(3,Node(5),Node(6)),Node(4,Node(7)))

#print all the leaf nodes

def print_leaf_node(root):
    if root:
        if not root.left and not root.right:
            print(root.data)
            
        print_leaf_node(root.left)
        print_leaf_node(root.right)
            
# print(print_leaf_node(a))
