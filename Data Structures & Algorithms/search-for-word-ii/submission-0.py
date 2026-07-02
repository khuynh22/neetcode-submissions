class TrieNode():
    def __init__(self):
        self.children = {}
        self.is_word = False
    def addWord(self, word: str) -> None:
        curr = self
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.is_word = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ROWS, COLS = len(board), len(board[0])
        visit, res = set(), set()
        root = TrieNode()
        for w in words:
            root.addWord(w)
        def backtracking(r, c, node, word):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or (r, c) in visit or board[r][c] not in node.children:
                return
            
            visit.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.is_word:
                res.add(word)
            
            backtracking(r + 1, c, node, word)
            backtracking(r - 1, c, node, word)
            backtracking(r, c + 1, node, word)
            backtracking(r, c - 1, node, word)

            visit.remove((r,c))

        for i in range(ROWS):
            for j in range(COLS):
                backtracking(i, j, root, "")
        
        return list(res)