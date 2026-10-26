class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        

        def backtracking(i,j,k):
            if len(word) == k:
                return True
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[k]:
                return False


            temp = board[i][j]
            board[i][j] = '#' 
            
            found = (backtracking(i + 1, j, k + 1) or 
                    backtracking(i - 1, j, k + 1) or 
                    backtracking(i, j + 1, k + 1) or 
                    backtracking(i, j - 1, k + 1))
                    
            board[i][j] = temp
            
            return found

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if backtracking(i,j,0):
                        return True
        return False
