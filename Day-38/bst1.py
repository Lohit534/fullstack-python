class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def insert(root, val):
    if root is None:
        return TreeNode(val)
    if val < root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)
    return root


def find_nth_largest(root, n):
    count = [0]
    result = [None]

    def reverse_inorder(node):
        if not node or result[0] is not None:
            return

        reverse_inorder(node.right)

        count[0] += 1
        if count[0] == n:
            result[0] = node.val
            return

        reverse_inorder(node.left)

    reverse_inorder(root)
    return result[0]



values = list(map(int, input().split()))
n = int(input("Enter nth element: "))


bst_root = None
for v in values:
    bst_root = insert(bst_root, v)


nth_largest = find_nth_largest(bst_root, n)
print(nth_largest)
