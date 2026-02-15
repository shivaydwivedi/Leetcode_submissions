 
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False


class StreamChecker:

    def __init__(self, words):
        self.root = TrieNode()
        self.stream = []
        self.maxLength = 0

        for word in words:
            self.maxLength = max(self.maxLength, len(word))
            self._insert(word[::-1])

    def _insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.isWord = True

    def query(self, letter):
        self.stream.append(letter)

        if len(self.stream) > self.maxLength:
            self.stream.pop(0)

        node = self.root

        for char in reversed(self.stream):
            if char not in node.children:
                return False
            node = node.children[char]
            if node.isWord:
                return True

        return False


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)