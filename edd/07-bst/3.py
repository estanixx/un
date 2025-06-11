class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.leaf = True


class BinarySearchTree:

    def __init__(self):
        self.leafs = 0
        self.height = 0
        self.root = None

    def insert(self, key):
        self.root = self._insertRecursively(self.root, key, 1)

    def _insertRecursively(self, root, key, height):
        self.height = max(self.height, height)
        if root is None:
            # One leaf more.
            self.leafs += 1
            return Node(key)
        # One leaf less.
        if root.leaf:
            root.leaf = False
            self.leafs -= 1
        if key < root.key:
            root.left = self._insertRecursively(root.left, key, height + 1)
        elif key > root.key:
            root.right = self._insertRecursively(root.right, key, height + 1)
        return root

    def search(self, key):
        if self._searchRecursively(self.root, key) != None:
            return True
        else:
            return False

    def _searchRecursively(self, root, key):
        if root is None or root.key == key:
            return root
        if key < root.key:
            return self._searchRecursively(root.left, key)
        return self._searchRecursively(root.right, key)

    def delete(self, key):
        self.root = self._deleteRecursively(self.root, key)

    def _deleteRecursively(self, root, key):
        if root is None:
            return root
        if key < root.key:
            root.left = self._deleteRecursively(root.left, key)
        elif key > root.key:
            root.right = self._deleteRecursively(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            root.key = self._minValueNode(root.right).key
            root.right = self._deleteRecursively(root.right, root.key)
        return root

    def _minValueNode(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def inOrder(self):
        elements = []
        self._inOrderRecursively(self.root, elements)
        return elements

    def _inOrderRecursively(self, root, elements):
        if root:
            self._inOrderRecursively(root.left, elements)
            elements.append(root.key)
            self._inOrderRecursively(root.right, elements)


for _ in range(int(input())):
    tree = BinarySearchTree()
    tuple(map(lambda val: tree.insert(int(val)), input().split()[:-1]))
    print(tree.leafs)
