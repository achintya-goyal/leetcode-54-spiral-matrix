class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix)
        i=1
        lst = []
        while matrix:
            lst += matrix.pop(0)

            if matrix:
                for row in matrix:
                    if row:
                        lst.append(row.pop())
            if matrix:
                lst+=matrix.pop()[::-1]
            if matrix:
                for row in matrix[::-1]:
                    if row:
                        lst.append(row.pop(0))
        return lst
