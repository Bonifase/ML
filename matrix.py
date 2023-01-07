class Matrix:

    def __init__(self, matrix=[[]]):
        self.matrix = matrix
        self.rows = len(self.matrix)
        self.columns = len(self.matrix[0]) if self.rows > 0 else 0


    def shape(self):
        """View dimensions

        Returns:
            tuple: containing rows and columns.
        """
        return (self.rows, self.columns)

    def determinant(self):
        """Matrix Determinant:
        """
        pass

    def transpose(self):
        """'Matrix Transpose:
        """
        pass

    def identity_mat(self):
        """Product of matrix and its inverse:
        """
        pass

    def inverse(self):
        """'Matrix inverse
        """
        pass

    def diagonal_difference(self):
        vert_diagonal, hor_diagonal = 0, 0

        for i in range(self.rows):
            vert_diagonal += (float(self.matrix[i-1][i-1]))

        for i in range(self.rows-1, -1, -1):
            hor_diagonal += (float(self.matrix[i][self.columns-1-i]))

        return vert_diagonal - hor_diagonal



M = [
    [1, 5, 2],
    [4, 7, 4],
    [2, 0, 9]
]

matrix = Matrix(M)

print(matrix.diagonal_difference())
