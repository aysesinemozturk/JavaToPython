package Matrix;

public class MatrixJava{
    //This class represents matrix structure.

    //attributes of the matrix
    public int numberOfRows;
    public int numberOfColumns;
    public int[][] values;

    //A constructor that gets attributes as parameters initializes empty values in the matrix based on its parameters.
    public MatrixJava(int NumberOfRows, int NumberOfColumns){
        this.numberOfRows = NumberOfRows;
        this.numberOfColumns = NumberOfColumns;
        values = new int[this.numberOfRows][this.numberOfColumns];
    }

    //A constructor gets again matrix's attributes as parameters, however this time it also takes vectorvalues which was
    //given already in the main method is prepared for the matrix's values. 
    //If vectorvalues length is same as our matrix's dimension, it will take it as values.
    //Otherwise, values of the matrix remains as zero, null.

    public MatrixJava(int NumberOfRows, int NumberOfColumns, int[] vectorValues){
        if(vectorValues.length != NumberOfColumns * NumberOfRows){
            System.out.println("the vectorValues array is not suitable for the matrix dimension.");
        }else{
            this.numberOfRows = NumberOfRows;
            this.numberOfColumns = NumberOfColumns;
            values = new int[this.numberOfRows][this.numberOfColumns];
            
            for(int i=0; i < this.numberOfRows; i++){
                for(int j=0; j< this.numberOfColumns; j++){
                    values[i][j] = vectorValues[i*this.numberOfColumns + j];
                }
            }
        }
    }

    //sum up two matrixes which are defined in main method.
    public MatrixJava sum(MatrixJava matrix){
        if(this.numberOfRows == matrix.numberOfRows && this.numberOfColumns == matrix.numberOfColumns){
            MatrixJava resultMatrix = new MatrixJava(this.numberOfRows, this.numberOfColumns);
            
            for(int i=0; i < this.numberOfRows; i++){
                for(int j= 0; j< this.numberOfColumns; j++){
                    resultMatrix.values[i][j] = values[i][j] + matrix.values[i][j];
                }
            }
            return resultMatrix;
        }else{
            return null;
        }
    }

    //report the result matrix object to the console
    public void report(){
        
        for(int i = 0; i < numberOfRows; i++) {
            System.out.print("|");
            for(int j = 0; j < numberOfColumns; j++) {
                System.out.print(values[i][j]);
                if(j < numberOfColumns - 1) {
                    System.out.print(",");
                }
            }
            System.out.println("|");
        }
    }
}