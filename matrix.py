import numpy as np


a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([[7, 8, 9, 10], [11, 12, 13, 14], [15, 16, 17, 18]])


c_numpy = np.dot(a, b)
print("Perkalian Matriks dengan Numpy:\n", c_numpy)


def multiply_matrices(mat1, mat2):
    
    rows_mat1, cols_mat1 = len(mat1), len(mat1[0])
    rows_mat2, cols_mat2 = len(mat2), len(mat2[0])
    if cols_mat1 != rows_mat2:
        raise ValueError("Matriks tidak dapat dikalikan.")
    
    
    result = [[0 for _ in range(cols_mat2)] for _ in range(rows_mat1)]
    
    
    for i in range(rows_mat1):
        for j in range(cols_mat2):
            for k in range(cols_mat1):
                result[i][j] += mat1[i][k] * mat2[k][j]
    return result

c_manual = multiply_matrices(a.tolist(), b.tolist())
print("Perkalian Matriks tanpa Library:\n", c_manual)
