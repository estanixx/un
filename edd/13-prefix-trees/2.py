from collections import deque

class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.count = 0

    def insert(self, word):
        node = self.root
        for char in word:
            node.count += 1
            # Me paro en el hijo y en su defecto creo uno.
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        # Si ya está pero no es un fin de palabra, añado.
        if not node.is_end_of_word:
            node.is_end_of_word = True
            node.count += 1
            self.count += 1

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def startsWithPrefix(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return len(node.children) > 0
    
    def wordsWithPrefix(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return 0
            node = node.children[char]
        return node.count

    def delete(self, word):
        q = deque()
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            else:
                q.append(node)
                node = node.children[char]
        if len(node.children) > 0:
            node.is_end_of_word = False
        else:
            for char in word[::-1]:
                node = q.pop()
                node.children.pop(char)
                if node.is_end_of_word or len(node.children) > 0:
                    break
            self.count -= 1
            return True

    def _traverseRecursively(self, node, current_word, words_list):
        if node.is_end_of_word:
            words_list.append(current_word)
        for char, child_node in node.children.items():
            self._traverseRecursively(child_node, current_word + char, words_list)

    def traverse(self):
        words_list = []
        self._traverseRecursively(self.root, '', words_list)
        return words_list
    
glosario = Trie()
for _ in range(int(input())):
    glosario.insert(input())
for _ in range(int(input())):
    pref = input()
    print(glosario.wordsWithPrefix(pref))
    