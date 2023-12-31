
class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.count += 1

    def find(self, word):
        node = self.root
        for i, char in enumerate(word):
            if node.children[char].count == 1:
                return i + 1
            node = node.children[char]
        return len(word)


def solution(words):
    trie = Trie()
    for word in words:
        trie.insert(word)

    return sum(trie.find(word) for word in words)


# 테스트
print(solution(["go", "gone", "guild"]))  # 7
print(solution(["abc", "def", "ghi", "jklm"]))  # 4
print(solution(["word", "war", "warrior", "world"]))  # 15