class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfString = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insertString(self,word):
        current = self.root
        for i in word:
            ch = i
            node = current.children.get(ch) 
            if node == None: # Checks if the char is in the Trie
                node = TrieNode()
                current.children.update({ch:node})
            current = node
        current.endOfString = True # End the string after insertion
        print("Successfully inserted")
    
    def search(self,word):
        current = self.root
        for i in word:
            node = current.children.get(i)
            if node == None:
                return False
            else:
                current = node
        # Eventhough it exists in the Trie, we have to make sure that it is not the prefix
        # by checking whether the next node's endOfString property set to True
        if current.endOfString == True:
            return True
        # Otherwise, it is the prefix, not the whole word
        else:
            return False
 
    def remove(self,root,word,index):
        ch = word[index]
        current = root.children.get(ch)
        canBeRemoved = False

        if len(current.children)>1:
            self.remove(current,word,index+1)
            return False
        
        if index == len(word)-1:
            if len(current.children) >= 1:
                current.endOfString = False
                return False
            else:
                root.children.pop(ch)
                return True 
        
        if current.endOfString == True:
            self.remove(current,word,index)
            return False
        
        canBeRemoved = self.remove(current,word,index+1)
        if canBeRemoved == True:
            root.children.pop(ch)
            return True
        else:
            return False
