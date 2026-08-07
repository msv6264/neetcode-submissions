class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        boxes = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]

        for i in range(9):
            row = set()

            for j in range(9):
                ele = board[i][j]

                if ele == '.':
                    continue
                
                box = (i // 3) * 3 + (j // 3)

                if ele in row or ele in cols[j] or ele in boxes[box]:
                    return False

                row.add(ele)
                cols[j].add(ele)
                boxes[box].add(ele)

        return True