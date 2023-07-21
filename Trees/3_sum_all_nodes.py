from Nodes import Node

a = Node(2,Node(3,Node(5),Node(6)),Node(4,Node(7)))

#sum of all nodes in a tree using recursion

def sum_all(root):
    if root:
        return root.data + sum_all(root.left) + sum_all(root.right)
    return 0

# print(sum_all(a))
