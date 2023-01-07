class Matrix:

    def __init__(self, matrix=[[]]):
        self.matrix = matrix
        self.rows = len(self.matrix)
        self.columns = len(self.matrix[0]) if self.rows > 0 else 0

    def diagonal_differece(self):
        vert_diagonal, hor_diagonal = 0, 0

        for i in range(self.rows):
            vert_diagonal += (float(self.matrix[i-1][i-1]))

        for i in range(self.rows-1, -1, -1):
            hor_diagonal += (float(self.matrix[i][self.columns-1-i]))

        return vert_diagonal - hor_diagonal


M = [
    ['9', '5', '7'],
    ['8', '3', '0'],
    ['6', '4', '1']
]
result = Matrix(M).diagonal_differece()
print(result)
