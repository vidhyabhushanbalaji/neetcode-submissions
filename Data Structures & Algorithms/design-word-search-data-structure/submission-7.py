class WordDictionary:

    def __init__(self):
        self.trie={".":"."}
    
    def addWord(self, word: str) -> None:
        currMap = self.trie
        for i in word:
            if i not in currMap:
                currMap[i]={}
            currMap = currMap[i]
        currMap["."] = "."

    def search(self, word: str) -> bool:
        queue = [self.trie]
        for i in word:
            for _ in range(len(queue)):
                if i ==".":
                    for k in queue[0]:
                        if k!=".":
                            queue.append(queue[0][k])
                else:
                    if i in queue[0]:
                        queue.append(queue[0][i])
                queue.pop(0)
        for i in queue:
            if "." in i:
                return True
        return False

