class TrieNode():
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie():
    def __init__(self):
        self.root = TrieNode()

    def insert(self,word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True
    
    def search(self,word):
        node =self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end

    def collect_words(self,node=None , prefix ="",words=None):
        if words is None:
            words= []
        if node is None:
            node = self.root
        if node.is_end:
            words.append(prefix)
        for char, child in node.children.items():
            self.collect_words(child, prefix+char, words)
        return words
    
    def start_with(self,prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        return self.collect_words(node,prefix)
    
    def autocomplete(self,prefix):
        node =self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        words = []
        self.collect_words(node,prefix,words)
        return words
    
trie = Trie()
trie.insert("apple")
trie.insert("app")
trie.insert("bat")
trie.insert("ball")
trie.insert("banana")
print(trie.search("bat"))
print("Stored Words in Trie:")
print(trie.collect_words())
print(trie.start_with("b"))
print(trie.autocomplete("a"))