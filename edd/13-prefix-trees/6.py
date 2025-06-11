from collections import deque

class TrieNode:
    def __init__(self, value=""):
        self.children = {}
        self.end = False  # Marks the end of a word
        self.value = value  # Character stored in the node
        self.count = 0  # Number of times the prefix is used
        self.word_count = 0  # Number of times the word is inserted

class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.total_words = 0  # Total unique words in the Trie

    def insert(self, word):
        """Inserts a word into the Trie."""
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode(char)
            node = node.children[char]
            node.count += 1  # Increment prefix count
        if not node.end:
            node.end = True
            self.total_words += 1
        node.word_count += 1  # Increment word count

    def search(self, word):
        """Searches for a word in the Trie and returns its count and the word."""
        node = self.root
        for char in word:
            if char not in node.children:
                return (0, word)  # Word not found
            node = node.children[char]
        return (node.word_count, word) if node.end else (0, word)

    def starts_with_prefix(self, prefix):
        """Checks if any word in the Trie starts with the given prefix."""
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

    def delete(self, word):
        """Deletes a word from the Trie."""
        stack = deque()
        node = self.root
        for char in word:
            if char not in node.children:
                return False  # Word not found
            stack.append((node, char))
            node = node.children[char]
        if not node.end:
            return False  # Word not found

        node.end = False
        node.word_count = 0
        self.total_words -= 1

        # Remove unused nodes
        while stack:
            parent, char = stack.pop()
            child = parent.children[char]
            if not child.children and not child.end:
                del parent.children[char]
            else:
                break
        return True

    def dfs_prefix(self, prefix):
        """Returns all words starting with the given prefix."""
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        words = []
        self._dfs_traverse(node, prefix, words)
        return words

    def _dfs_traverse(self, node, current_word, words):
        """Helper function for DFS traversal."""
        if node.end:
            words.append((current_word, node.word_count))
        for char, child in node.children.items():
            self._dfs_traverse(child, current_word + char, words)

def process_text(text):
    """Processes the input text by removing punctuation and converting to lowercase."""
    punctuation = ",.;:?!-"
    translator = str.maketrans("", "", punctuation)
    return text.translate(translator).lower().split()

def main():
    # Input processing
    L = int(input())
    text = ""
    for _ in range(L):
        text += input() + " "
    words = process_text(text)

    # Build Trie
    trie = Trie()
    for word in words:
        trie.insert(word)

    # Query processing
    C = int(input())
    for _ in range(C):
        prefix = input()
        matching_words = trie.dfs_prefix(prefix)
        if not matching_words:
            print("-")
            continue

        # Sort by frequency (descending) and lexicographical order
        matching_words.sort(key=lambda x: (-x[1], x[0]))
        result = [word for word, _ in matching_words]
        print(" ".join(result))

if __name__ == "__main__":
    main()