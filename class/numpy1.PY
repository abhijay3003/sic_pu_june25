import numpy as np
from scipy import stats
# to print mean ,mode,median
'''array = np.array([[1,2,4,3,1,4,2,5,6,1,2]])
mean = np.mean(array)
median = np.median(array)
mode = stats.mode(array)
print(mean,median)
print("Mode:", mode.mode, "Count:", mode.count)'''
# to print the zero matrix in 1D
'''array1=np.zeros(3)
print(array1)'''
# to print the zero matrix in 4 coloum and 1 rows 
'''array2=np.zeros((1,4))
array3=np.zeros((2,5))
print(array2)
print(array3)'''
# to exceess the ecah element in the matrix we use here 1st rows is array[0][0]
''' print(array2[0][0])'''
'''the type is ndarray '''
# to print the matrixwith full of matrix vlues but of same value
"""array1 = np.full((2,4),5)
print(array1)"""
# to orint the matrix with difffernt data type 
"""array1 = np.full((2,4),5  , dtype = float)
print(array1)"""
#to print the numbers in order
'''array1= np.arange(10) or array1= np.array(0,10,1)
print(array1)''' #[0 1 2 3 4 5 6 7 8 9]
#to print the matrxis with ones
''' array1 = np.ones(10)
array2 = np.ones((1,3))
print(array1) '''
# shape is used to determine the stures of matrix
''' vector = np.arange(5)
print('Vector shape:', vector.shape) # (5,)
matrix = np.ones([3, 2])
print('Matrix shape:', matrix.shape) # (3,2)
tensor = np.zeros([2, 3, 3])
print('Tensor:', tensor)
print("Tensor shape:", tensor.shape) '''# (2,3,3)
# to reshAPE    the give matrxis 
"""arr = np.arange(1, 10)
print(arr, '\n')  # [1 2 3 4 5 6 7 8 9] 
# Reshape to 3x3 matrix
arr = arr.reshape(3, 3)
print(arr, '\n') # [[1 2 3]
                   [4 5 6] 
                   [7 8 9]]
# Reshape back to the original size
arr = arr.reshape(9)
print(arr)    [1 2 3 4 5 6 7 8 9]
arr = arr.reshape(2, 5) # ValueError
print(arr) """
# to donot give the coloume number just enter the -1 it decide itself 
'''arr = np.arange(1, 10).reshape(3, -1) ''' # Here python infers/decides the number of columns by itself.
''' arr7 = arr2.reshape(-1, 4) # Numpy predicts and fixes number of rows
arr8 = arr2.reshape(-1, -1) #ValueError. Can only specify one unknown dimension '''
  # import pdb
 # pdb.set_trace() # debug     #  sooooo important
matrix1 = np.array([[3, 4, 5], [2, 6, 9]])
matrix2 = np.array([[3, 4], [3, 5], [2, 6]])

matrix3 = np.dot(matrix1, matrix2)

print('Matrix3=\n', matrix3)
