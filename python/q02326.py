"""
2326. Spiral Matrix IV

You are given two integers `m` and `n`, which represent the dimensions of a
matrix.

You are also given the `head` of a linked list of integers.

Generate an `m x n` matrix that contains the integers in the linked list
presented in spiral order (clockwise), starting from the top-left of the
matrix. If there are remaining empty spaces, fill them with `-1`.

Return the generated matrix.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    @staticmethod
    def matrix_string(matrix: List[List[int]]) -> str:
        """Returns a formatted string of `matrix` in the style of numpy"""
        m, n = len(matrix), len(matrix[0])  # rows, columns
        max_width = 1  # max element width in characters
        mtx_strings = [['' for j in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                mtx_strings[i][j] = str(matrix[i][j])
                if len(mtx_strings[i][j]) > max_width:
                    max_width = len(mtx_strings[i][j])
        return '[' + ',\n '.join(('[' + ', '.join("{entry: >{pad}}".format(entry=mtx_strings[i][j], pad=max_width) for j in range(n)) + ']') for i in range(m)) + ']'


    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        """O(m * n) time, O(m * n) space solution"""
        node = head
        mtx = [[-1] * n for i in range(m)]
        pos = [0, 0]  # initial write location
        vel_array = [[0, 1], [1, 0], [0, -1], [-1, 0]]  # circular array of velocities
        vel_idx = 0

        while node:
            mtx[pos[0]][pos[1]] = node.val
            # if next position is inside matrix and mtx[next_position] is -1,
            if (0 <= pos[0] + vel_array[vel_idx][0] < m) and \
               (0 <= pos[1] + vel_array[vel_idx][1] < n) and \
               (mtx[pos[0] + vel_array[vel_idx][0]][pos[1] + vel_array[vel_idx][1]] == -1):
                pos[0] += vel_array[vel_idx][0]
                pos[1] += vel_array[vel_idx][1]
            else:  # if not true, rotate velocity vector
                vel_idx = (vel_idx + 1) % len(vel_array)
                pos[0] += vel_array[vel_idx][0]
                pos[1] += vel_array[vel_idx][1]
            node = node.next
        return mtx