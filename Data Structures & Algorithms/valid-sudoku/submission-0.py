class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)
        
        for r in range(9):
            for c in range(9):
                num = board[r][c]

                if num == '.':
                    continue
                
                if num in rows[r]:
                    return False 
                rows[r].add(num)

                if num in cols[c]:
                    return False 
                cols[c].add(num)

                if num in boxes[(r // 3, c // 3)]:
                    return False
                boxes[(r // 3, c // 3)].add(num)
        return True