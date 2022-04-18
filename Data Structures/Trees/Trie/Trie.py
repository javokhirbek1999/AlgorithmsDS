class TrieNode:

    def __init__(self, char) -> None:
        self.char = char
        self.children = {}
        self.count = 0
        self.end = False

class Trie:

    def __init__(self) -> None:
        self.root = TrieNode("")
    
    def add(self, word:str):

        node = self.root

        for char in word:

            if char in node.children:
                node = node.children[char]
            else:
                newNode = TrieNode(char)
                node.children[char] = newNode
                node = newNode

        node.end = True
        node.count += 1 
    
    def dfs(self, node, prefix):

        if node.end:
            self.output.append((prefix + node.char, node.count))
        
        for child in node.children.values():
            self.dfs(child, prefix + node.char)

    def query(self, word:str):

        self.output = []
        node = self.root

        for char in word:

            if char in node.children:
                node = node.children[char]
            else:
                return []
        
        self.dfs(node, word[:-1])


        return sorted(self.output, key=lambda x:x[1], reverse=True)
