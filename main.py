class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def preorder(root):
    if root is None:
        return []
    return [root.data] + preorder(root.left) + preorder(root.right)


def inorder(root):
    if root is None:
        return []
    return inorder(root.left) + [root.data] + inorder(root.right)


def postorder(root):
    if root is None:
        return []
    return postorder(root.left) + postorder(root.right) + [root.data]


# Build the tree based on Cathrine's layout
root = Node("C")

# Left side of C -> A
root.left = Node("A")
root.left.left = Node("H")
root.left.left.left = Node("E")
root.left.left.right = Node("C")

root.left.right = Node("R")
root.left.right.left = Node("A")
root.left.right.right = Node("J")

# Right side of C -> T
root.right = Node("T")
root.right.left = Node("I")
root.right.left.left = Node("E")

root.right.right = Node("N")
root.right.right.left = Node("S")


if __name__ == "__main__":
    print("Preorder :", ", ".join(preorder(root)))
    print("Inorder  :", ", ".join(inorder(root)))
    print("Postorder:", ", ".join(postorder(root)))