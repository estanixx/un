class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
        self.count = 0
 
class Trie:
    def __init__(self):
        self.root = TrieNode()
 
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.count += 1
        node.end = True
 
    def mostUsedPrefix(self):
        node = self.root
        prefix = ""
        while len(node.children) == 1 and not node.end:
            char = next(iter(node.children))
            if node.children[char].count < 2:
                break
            prefix += char
            node = node.children[char]
        return prefix if prefix else '-'
 
while True:
    T = int(input())
    if T == 0:
        break
    arbol = Trie()
    for i in range(T):
        arbol.insert(input())
    longest_prefix = arbol.mostUsedPrefix()
    print(longest_prefix)