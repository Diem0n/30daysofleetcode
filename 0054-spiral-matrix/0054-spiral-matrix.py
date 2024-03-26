class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        rows, cols = len(matrix), len(matrix[0])
        result = []
        top, bottom, left, right = 0, rows - 1, 0, cols - 1
        direction = 0 

        while top <= bottom and left <= right:
            if direction == 0:  
                for col in range(left, right + 1):
                    result.append(matrix[top][col])
                top += 1

            elif direction == 1:  
                for row in range(top, bottom + 1):
                    result.append(matrix[row][right])
                right -= 1

            elif direction == 2: 
                for col in range(right, left - 1, -1):
                    result.append(matrix[bottom][col])
                bottom -= 1

            else: 
                for row in range(bottom, top - 1, -1):
                    result.append(matrix[row][left])
                left += 1

            direction = (direction + 1) % 4  

        return result
