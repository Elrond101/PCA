#输入几个n维的点，将其通过最小的误差压缩为l维
import numpy as np
matrix = np.array([
    [1, 2, 3, 10, 5, 6],
    [7, 8, 9, 50, 8, 40],
    [4, 5, 6, 90, 8, 9],]) #矩阵中每一行都代表一个点
print(f"原矩阵为\n{matrix}")
S = np.matmul(matrix.T, matrix) #计算协方差矩阵
eigenvalue, featurevector = np.linalg.eigh(S)
l = 5 #压缩的目标维度
D = featurevector[0:l,:] #解码矩阵
c = np.matmul(np.rot90(D).T, np.rot90(matrix)) #压缩结果
print(f"压缩为{l}维后变为\n{np.rot90(c)}")
x = np.rot90(np.matmul(np.rot90(D), c),k = 3) #解压结果
print(f"解压后为\n{x}")