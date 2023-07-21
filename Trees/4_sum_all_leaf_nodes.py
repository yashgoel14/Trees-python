from Nodes import Node

a = Node(2,Node(3,Node(5),Node(6)),Node(4,Node(7)))

#print sum of all the leaf nodes

def sum_leaf_root(root):
    if root:
        if root.left or root.right:
            return sum_leaf_root(root.left) + sum_leaf_root(root.right)
        return root.data
    return 0

# print(sum_leaf_root(a))
