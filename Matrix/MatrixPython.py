from array import *
class MatrixPython:
    
    #numberOfRows = 0
    #numberOfColumns = 0
    #values = [5][5]

    # A constructor that gets attributes as parameters initializes empty values in the matrix based on its parameters.
    def __init__(self, NumberOfRows, NumberOfColumns):
        self.numberOfRows = NumberOfRows
        self.numberOfColumns = NumberOfColumns
        values = [self.numberOfRows][self.numberOfColumns]

    # A constructor gets again matrix's attributes as parameters, however this time it also takes vectorvalues which was
    # given already in the main method is prepared for the matrix's values. 
    # If vectorvalues length is same as our matrix's dimension, it will take it as values.
    # Otherwise, values of the matrix remains as zero, null.

    def __init__(self, NumberOfRows, NumberOfColumns, vectorValues):
        if(vectorValues.length != NumberOfColumns * NumberOfRows):
            print('the vectorValues array is not suitable for the matrix dimension.')
        else:
            self.numberOfRows = NumberOfRows
            self.numberOfColumns = NumberOfColumns
            values = [self.numberOfRows][self.numberOfColumns]

            for i in range (0,self.numberOfRows):
                for j in range(0,self.numberOfColumns):
                    values[i][j] = vectorValues[i*self.numberOfColumns + j]

    # sum up two matrixes which are defined in main method.
    def sum(self, matrix):
        if(self.numberOfRows == matrix.numberOfRows and self.numberOfColumns == matrix.numberOfColumns):
            resultMatrix = MatrixPython(self.numberOfRows, self.numberOfColumns)

            for i in range (0,self.numberOfRows):
                for j in range(0,self.numberOfColumns):
                    resultMatrix.values[i][j] = self.values[i][j] + matrix.values[i][j]
            
            return resultMatrix
        else:
            return None
    
    #report the result matrix object to the console
    def report(self):
        
        for i in range(0,self.numberOfRows):
            print('|')
            for j in range(0, self.numberOfColumns):
                print(self.values[i][j])
                if(j < numberOfColumns - 1):
                    print('','')
            
            print('|')


