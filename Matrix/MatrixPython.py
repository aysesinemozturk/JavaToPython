from __future__ import print_function
from array import *

class MatrixPython:
    
    #numberOfRows = 0
    #numberOfColumns = 0
    #values = []

   

    # A constructor gets again matrix's attributes as parameters, however this time it also takes vectorvalues which was
    # given already in the main method is prepared for the matrix's values. 
    # If vectorvalues length is same as our matrix's dimension, it will take it as values.
    # Otherwise, values of the matrix remains as zero, null.

    def __init__(self, NumberOfRows, NumberOfColumns, vectorValues = None):
        
        self.numberOfRows = NumberOfRows
        self.numberOfColumns = NumberOfColumns
        
        if(vectorValues == None):
            self.values = [ [ 0 for y in range( self.numberOfColumns ) ] for x in range( self.numberOfRows ) ]
        
        elif(len(vectorValues) != NumberOfColumns * NumberOfRows):
            
            print('the vectorValues array is not suitable for the matrix dimension.')
            self.values = [ [ 0 for y in range( self.numberOfColumns ) ] for x in range( self.numberOfRows ) ]
        
        else:
           
            self.values = [ [ 0 for y in range( self.numberOfColumns ) ] for x in range( self.numberOfRows ) ]

            for i in range (self.numberOfRows):
                for j in range(self.numberOfColumns):
                    self.values[i][j] = vectorValues[i *self.numberOfColumns + j]

    # sum up two matrixes which are defined in main method.
    def sum(self, matrix):
        if(self.numberOfRows == matrix.numberOfRows and self.numberOfColumns == matrix.numberOfColumns):
            resultMatrix = MatrixPython(self.numberOfRows, self.numberOfColumns)

            for i in range (self.numberOfRows):
                for j in range(self.numberOfColumns):
                    resultMatrix.values[i][j] = self.values[i][j] + matrix.values[i][j]
            
            return resultMatrix
        else:
            return None
    
    #report the result matrix object to the console
    def report(self):
        
        for i in range(self.numberOfRows):
            print('|', end='')
            for j in range(self.numberOfColumns):
                print(self.values[i][j],end ='')
                if(j < self.numberOfColumns - 1):
                    print(',',end ='')
            
            print('|')


