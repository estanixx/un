class TrieNode:
    def __init__(self):
        self.children = {}
        self.prefix_count = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.prefix_count += 1

    def delete(self, word):
        node = self.root
        stack = []
        for char in word:
            if char not in node.children:
                return False
            stack.append((node, char))
            node = node.children[char]
        if node.prefix_count > 0:
            for parent, char in stack:
                parent.children[char].prefix_count -= 1
                if parent.children[char].prefix_count == 0:
                    del parent.children[char]
            return True
        return False

    def commonPrefix(self, k, h):
        def dfs(node, depth):
            if depth == h:
                return node.prefix_count >= k
            for char, child in node.children.items():
                if dfs(child, depth + 1):
                    return True
            return False

        return dfs(self.root, 0)

def main():
    P = int(input())
    arbol = Trie()

    for _ in range(P):
        entrada = input().split()
        tipo = entrada[0]
        if tipo == "1":
            arbol.insert(entrada[1])
        elif tipo == "2":
            arbol.delete(entrada[1])
        elif tipo == "3":
            k = int(entrada[1])
            h = int(entrada[2])
            if arbol.commonPrefix(k, h):
                print("SI")
            else:
                print("NO")

if __name__ == "__main__":
    main()