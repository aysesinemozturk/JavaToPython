package Matrix;

public class Main {

    public static void main(String[] args){
       
        //our vectorValues integer arrays
        int[] vector1 = {1,2,3,4,5,6,7,8,9,10,11,12};
        int[] vector2 = {11,22,33,44,55,66,77,88,99,100,111,122};

        //our MatrixJava objects
        MatrixJava matrix1 = new MatrixJava(3,4, vector1);
        MatrixJava matrix2 = new MatrixJava(3,4, vector2);

        matrix1.report();
        matrix2.report();

        MatrixJava resultMatrix = matrix1.sum(matrix2);
        if(resultMatrix !=null){
            resultMatrix.report();
        }
    }
}
