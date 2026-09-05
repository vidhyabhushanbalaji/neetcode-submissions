class PrefixTree:
    def __init__(self):
        self.trie={".":"."}

    def insert(self, word: str) -> None:
        insert = word+"."
        currMap = self.trie
        for i in insert:
            if not(i in currMap):
                currMap[i] = {}
            currMap = currMap[i]
        currMap["."]="."

    def search(self, word: str) -> bool:
        currMap = self.trie
        for i in word:
            if not(i in currMap):
                return False
            currMap = currMap[i]
        return ("." in currMap)

    def startsWith(self, prefix: str) -> bool:
        currMap = self.trie
        for i in prefix:
            if not(i in currMap):
                return False
            currMap = currMap[i]
        return True

