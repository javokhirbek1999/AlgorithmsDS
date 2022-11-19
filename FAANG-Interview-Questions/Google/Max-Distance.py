class TrieNode:
    def __init__(self, char: str) -> None:
        self.char = char
        self.children = {}
        self.end = False


class Trie:

    def __init__(self) -> None:
        self.root = TrieNode("")
    

    def add(self, word: str) -> None:

        node = self.root

        for char in word:

            if char in node.children:
                node = node.children[char]
            else:
                newNode = TrieNode(char)
                node.children[char] = newNode
                node = newNode
        
        node.end = True        

    
    def getMaxDistance(self) -> int:
        
        node = self.root.children

        if len(node) > 1:
            return 0

        while len(node) == 1:
            currentKey = list(node.keys())[0]
            node = node[currentKey].children

        
        return self.dfsLength(node, 0)
        
        

    def dfsLength(self, node, size):

        if len(node) == 0:
            return size
            

        total = 0
        for child in node.values():
            total += self.dfsLength(child.children, size+1)
        
        return total
        


def solve(binary_strings) -> int:

    trie = Trie()

    for string in binary_strings:
        trie.add(string)

    return trie.getMaxDistance()
