from MatrixPython import MatrixPython

#integer arrays of vectorValues
vector1 = [1,2,3,4,5,6,7,8,9,10,11,12]
vector2 = [11,22,33,44,55,66,77,88,99,100,111,122]

#MatrixPython objects
matrix1 = MatrixPython(3,4, vector1)
matrix2 = MatrixPython(3,4, vector2)

matrix1.report()
print('')
matrix2.report()
print('')

resultMatrix = matrix1.sum(matrix2)
if(resultMatrix != None):
    resultMatrix.report()
else:
    print "the summation of two matrixes is null!"