class Node(object):
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree(object):
    def __init__(self):
        self.size = 0
        self.root = None
        self.elements = []

    def insert(self, key):
        newNode = None
        if not self.search(key):
            newNode = self._insertRecursively(self.root, key)
            self.root = newNode
        return newNode

    def _insertRecursively(self, root, key):
        if not root:
            new_node = Node(key)
            self.elements.append(new_node)
            self.size += 1
            return new_node
        elif key < root.key:
            root.left = self._insertRecursively(root.left, key)
        else:
            root.right = self._insertRecursively(root.right, key)

        root.height = 1 + max(self.getNodeHeight(root.left),
                              self.getNodeHeight(root.right))

        balanceFactor = self.getNodeBalance(root)
        if balanceFactor > 1:
            if key < root.left.key:
                return self._rightRotate(root)
            else:
                root.left = self._leftRotate(root.left)
                return self._rightRotate(root)

        if balanceFactor < -1:
            if key > root.right.key:
                return self._leftRotate(root)
            else:
                root.right = self._rightRotate(root.right)
                return self._leftRotate(root)

        return root

    def delete(self, key):
        self.size -= self.search(key)
        self.root = self._deleteRecursively(self.root, key)

    def _deleteRecursively(self, root, key):

        if not root:
            return root
        elif key < root.key:
            root.left = self._deleteRecursively(root.left, key)
        elif key > root.key:
            root.right = self._deleteRecursively(root.right, key)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            temp = self._getMin(root.right)
            root.key = temp
            root.right = self._deleteRecursively(root.right, temp)
        if root is None:
            return root

        root.height = 1 + max(self.getNodeHeight(root.left), self.getNodeHeight(root.right))
        balanceFactor = self.getNodeBalance(root)

        if balanceFactor > 1:
            if self.getNodeBalance(root.left) >= 0:
                return self._rightRotate(root)
            else:
                root.left = self._leftRotate(root.left)
                return self._rightRotate(root)
        if balanceFactor < -1:
            if self.getNodeBalance(root.right) <= 0:
                return self._leftRotate(root)
            else:
                root.right = self._rightRotate(root.right)
                return self._leftRotate(root)
        return root

    def _leftRotate(self, z):
        y = z.right
        aux = y.left
        y.left = z
        z.right = aux
        z.height = 1 + max(self.getNodeHeight(z.left), self.getNodeHeight(z.right))
        y.height = 1 + max(self.getNodeHeight(y.left), self.getNodeHeight(y.right))
        return y

    def _rightRotate(self, z):
        y = z.left
        aux = y.right
        y.right = z
        z.left = aux
        z.height = 1 + max(self.getNodeHeight(z.left), self.getNodeHeight(z.right))
        y.height = 1 + max(self.getNodeHeight(y.left), self.getNodeHeight(y.right))
        return y
    
    @classmethod
    def getNodeHeight(cls, root):
        if not root:
            return 0
        return root.height
    
    @classmethod
    def getNodeBalance(cls, root):
        if not root:
            return 0
        return cls.getNodeHeight(root.left) - cls.getNodeHeight(root.right)

    @classmethod
    def isNodeBalanced(cls, root):
        if not root:
            return False
        if root.left and root.right:
            return cls.isNodeBalanced(root.left) and cls.isNodeBalanced(root.right) and cls.getNodeHeight(root.right) == cls.getNodeHeight(root.left)
        elif root.left is None and root.right is None:
            return True
        else:
            return False
        
    def _getMin(self, root):
        if root is None:
            return None
        elif root.left is None:
            return root.key
        return self._getMin(root.left)

    def _getMax(self, root):
        if root is None:
            return None
        elif root.right is None:
            return root.key
        return self._getMax(root.right)


    def search(self, key):
        return self._searchRecursively(self.root, key) != None

    def _searchRecursively(self, root, key):
        if root is None or root.key == key:
            return root
        if key < root.key:
            return self._searchRecursively(root.left, key)
        else:
            return self._searchRecursively(root.right, key)

    def inOrder(self):
        elements = []
        self._inOrderRecursively(self.root, elements)
        return elements

    def _inOrderRecursively(self, root, elements):
        if root:
            self._inOrderRecursively(root.left, elements)
            elements.append(root.key)
            self._inOrderRecursively(root.right, elements)

    def popMin(self):
        if self.size == 0:
            return None
        else:
            key = self._getMin(self.root)
            self.delete(key)
            return key
        
    def popMax(self):
        if self.size == 0:
            return None
        else:
            key = self._getMax(self.root)
            self.delete(key)
            return key
 

def scanTreeHeight(node, data):
    if not node:
        return
    if AVLTree.isNodeBalanced(node):
        data['max_height'] = max(data['max_height'], AVLTree.getNodeHeight(node))
    if node.right:
        scanTreeHeight(node.right, data)
    if node.left:
        scanTreeHeight(node.left, data)


def printTree(node, level=0):
    if not node:
        return
    if node.right:
        printTree(node.right, level+1)
    print('\t' * level + str(AVLTree.isNodeBalanced(node)))
    if node.left:
        printTree(node.left, level+1)
        

 
while (inp:=int(input())) != 0:
    avl = AVLTree()
    list(map(lambda a: avl.insert(int(a)), input().split()))
    data = {
        'max_height': 0
    }
    scanTreeHeight(avl.root, data)
    print(data['max_height'])
