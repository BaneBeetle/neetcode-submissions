class TrieNode:
    def __init__(self):
        self.word = False
        self.children = {}

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                new = TrieNode()
                curr.children[c] = new
            curr = curr.children[c]
        curr.word = True

    
    def search(self, word: str) -> bool:

        def dfs(i, node):
            if i >= len(word):
                return node.word
            
            if word[i] == ".":
                for child in node.children.values():
                    if dfs(i+1, child):
                        return True
                return False

            if word[i] not in node.children:
                return False
            
            return dfs(i+1, node.children[word[i]])

        return dfs(0, self.root)