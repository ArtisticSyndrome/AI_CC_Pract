def solveNQueens(n):
    col = set()
    diag1 = set()
    diag2 = set()
    
    result = []
    board = [['.' for _ in range(n)] for _ in range(n)]
    
    def backtrack(row):
        if row == n:
            result.append([''.join(r) for r in board])
            return
        
        for c in range(n):
            if c in col or row + c in diag1 or row - c in diag2:
                continue
            
            col.add(c)
            diag1.add(row + c)
            diag2.add(row - c)
            board[row][c] = 'Q'
            
            backtrack(row + 1)
            
            col.remove(c)
            diag1.remove(row + c)
            diag2.remove(row - c)
            board[row][c] = '.'
    
    backtrack(0)
    return result

def printSolutions(boards):
    for i, board in enumerate(boards):
        print(f"Solution {i + 1}:")
        for row in board:
            print(' '.join(row))
        print()

if __name__ == "__main__":
    boards = solveNQueens(4)
    printSolutions(boards)
