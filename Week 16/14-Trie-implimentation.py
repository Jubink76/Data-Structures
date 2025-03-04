class TrieNode:
    def __init__(self):
        self.children = {}  # Dictionary to store child nodes
        self.is_end_of_word = False  # Marks the end of a word

class Trie:
    def __init__(self):
        self.root = TrieNode()

    # Insert a word into Trie
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    # Search for a word in Trie
    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False  # Word not found
            node = node.children[char]
        return node.is_end_of_word  # Returns True if it's a valid word

    # Delete a word from Trie
    def delete(self, word, node=None, depth=0):
        if node is None:
            node = self.root
        if depth == len(word):
            if not node.is_end_of_word:
                return False  # Word does not exist
            node.is_end_of_word = False
            return len(node.children) == 0  # If no children, delete node
        char = word[depth]
        if char not in node.children:
            return False  # Word does not exist
        should_delete = self.delete(word, node.children[char], depth + 1)
        if should_delete:
            del node.children[char]
            return len(node.children) == 0
        return False

    # Find words with a given prefix
    def starts_with(self, prefix):
        def dfs(node, prefix):
            words = []
            if node.is_end_of_word:
                words.append(prefix)
            for char in node.children:
                words.extend(dfs(node.children[char], prefix + char))
            return words

        node = self.root
        for char in prefix:
            if char not in node.children:
                return []  # Prefix not found
            node = node.children[char]
        return dfs(node, prefix)  # Find all words starting with the prefix

    def collect_words(self,node = None,prefix="",words= None):
        if words is None:
            words =  []
        if node is None:
            node = self.root
        if node.is_end_of_word:
            words.append(prefix)
        for char, child in node.children.items():
            self.collect_words(child,prefix+char, words)
        return words
    
    

# Example Usage
trie = Trie()
trie.insert("apple")
trie.insert("app")
trie.insert("banana")
print(trie.collect_words())
print(trie.search("apple"))  # True
print(trie.search("appl"))   # False
print(trie.starts_with("ap")) # ['apple', 'app']
trie.delete("apple")
print(trie.search("apple"))  # False
