from typing import List

class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        # at first find the rooks position
        rook_pos = {'x': -1, 'y': -1}
        rookblocked = {'up': False, 'down': False, 'left': False, 'right': False}
        for i in range(8):
            for j in range(8):
                if board[i][j] == 'R':
                    rook_pos['x'] = i
                    rook_pos['y'] = j
                    break
            if rook_pos['x'] != -1:
                break   

        # now check in all 4 directions
        captures = 0
        # check upwards
        for i in range(rook_pos['x'] - 1, -1, -1):
            if board[i][rook_pos['y']] == 'B':
                break
            if board[i][rook_pos['y']] == 'p':
                captures += 1
                break
        # check downwards
        for i in range(rook_pos['x'] + 1, 8):
            if board[i][rook_pos['y']] == 'B':
                break
            if board[i][rook_pos['y']] == 'p':
                captures += 1
                break
        # check leftwards
        for j in range(rook_pos['y'] - 1, -1, -1):
            if board[rook_pos['x']][j] == 'B':
                break
            if board[rook_pos['x']][j] == 'p':
                captures += 1
                break
        # check rightwards
        for j in range(rook_pos['y'] + 1, 8):
            if board[rook_pos['x']][j] == 'B':
                break
            if board[rook_pos['x']][j] == 'p':
                captures += 1
                break
        return captures