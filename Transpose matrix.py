class Solution(object):
    def transpose(self, matrix):
        column = len(matrix[0])
        inv_matrix = [[0] * len(matrix) for i in range(column)]
        for i in range(column):
            for j in range(len(matrix)):
                inv_matrix[i][j] = matrix[j][i]
        return inv_matrix        
        
