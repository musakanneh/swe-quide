class Node(object):
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None


def insert(node, root):
    if root is None:
        root = node
        return

    if root.data < node.data:
        if root.right is None:
            root.right = node
        else:
            # recursively call the insert with right child of the root and the node
            insert(root.right, node)
    else:
        if root.left is None:
            root.left = node
        else:
            insert(root.left, node)


def search(node, key):
    print("Current Node is : ", node.data)
    if node is None:
        print("noting found")
        return

    if node.data == key:
        "Node exits"
        return node

    if node.data < key:
        return search(node.right, key)
    return search(node.left, key)


def preorder(node):
    if node is None:
        print(node.data)
        preorder(node.right)
        preorder(node.left)
        
def delete(node):
    pass


tree = Node(5)
insert(tree, Node(3))
insert(tree, Node(2))
insert(tree, Node(4))
insert(tree, Node(7))
insert(tree, Node(6))
insert(tree, Node(8))
# preorder(tree)
search(tree, 8)
