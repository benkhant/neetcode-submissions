class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        # brute force
        self.store = []

        # self.root = TrieNode()

    def addWord(self, word: str) -> None:
        self.store.append(word)

        # cur = self.root
        # for c in word:
        #     if c not in cur.children:
        #         cur.children[c] = TrieNode()
        #     cur = cur.children[c]
        # cur.endOfWord = True

    def search(self, word: str) -> bool:
        for w in self.store:
            if len(w) != len(word):
                continue
            i = 0
            while i < len(word):
                if word[i] == w[i] or word[i] == ".":
                    i += 1
                else:
                    break
            if i == len(word):
                return True
        return False
        
        # cur = self.root
        # for c in word:
        #     if c not in cur.children:
        #         return False
        #     elif c == ".":
        #         for child in cur.children.values():
                    
        #     cur = cur.children[c]
        # return cur.endOfWord

    