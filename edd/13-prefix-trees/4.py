class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0  # Number of times this node is visited

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.count += 1  # Increment the count for each node visited

    def find_minimal_unique_prefix(self, word):
        node = self.root
        prefix_length = 0
        for char in word:
            prefix_length += 1
            node = node.children[char]
            if node.count == 1:  # Unique prefix found
                return prefix_length
        return len(word)  # If no unique prefix, return the full length

def minimal_unique_prefix_length(names):
    trie = Trie()
    # Insert all names into the Trie
    for name in names:
        trie.insert(name)
    # Calculate the minimal unique prefix length for each name
    total_length = 0
    for name in names:
        total_length += trie.find_minimal_unique_prefix(name)
    return total_length

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    idx = 0
    while True:
        A = int(data[idx])
        idx += 1
        if A == 0:
            break
        names = []
        for _ in range(A):
            names.append(data[idx])
            idx += 1
        result = minimal_unique_prefix_length(names)
        print(result)

if __name__ == "__main__":
    main()