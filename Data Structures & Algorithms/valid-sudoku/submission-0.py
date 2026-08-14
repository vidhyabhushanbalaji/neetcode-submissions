class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        oneToNine = {"1","2","3","4","5","6","7","8","9"}
        rows = [oneToNine.copy() for i in range(9)]
        cols = [oneToNine.copy() for i in range(9)]
        squares = [[oneToNine.copy() for i in range(3)] for i in range (3)]
        for y in range(9):
            for x in range(9):
                try:
                    if (board[x][y]!="."):
                        rows[x].remove(board[x][y])
                        cols[y].remove(board[x][y])
                        squares[x//3][y//3].remove(board[x][y])
                except:
                    print(board[x][y])
                    return False
        return True



        