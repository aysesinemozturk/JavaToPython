package TSP;
import java.util.ArrayList;

public class enumaration{

    public static void main(String[] args) {
        long startTime = System.nanoTime();
        int[] nodeList = new int[5];
        for(int i=0;i<nodeList.length;i++) {
            nodeList[i] = i;
        }
        printArraylist(candidateRoutes(nodeList));
        long endTime = System.nanoTime();
        System.out.println("Execution time:"+(endTime-startTime)/1000000);
        }
    
        public static ArrayList<int[]> candidateRoutes (int[] nodeList){
            int[] tabuList = new int[0];
            int[] candidateList = nodeList;
            ArrayList<int[]> sol = new ArrayList<>();
            ArrayList<int[]> solution = giveSubarray(tabuList, candidateList, sol);
            return solution;
            }
    
        public static ArrayList<int[]> giveSubarray (int[] tabuList, int[] candidateList, ArrayList<int[]> solutionList){
            if (candidateList.length == 1){
                int[] tempTabu = add(tabuList, candidateList[0]);
                solutionList.add(tempTabu);
            }
            else{
                for(int i=0;i<candidateList.length;i++){
                    int[] tempTabu = add(tabuList, candidateList[i]);
                    int[] tempCandidate = remove(candidateList, i);
                    solutionList = giveSubarray(tempTabu, tempCandidate, solutionList);
    
                }
            }
            return solutionList;
        }
    
        public static int[] add (int[] vector, int element){
            int[] dummy = new int[vector.length+1];
            for (int i=0;i<dummy.length;i++){
                if (i != vector.length){
                    dummy[i] = vector[i];
                }
                else{
                    dummy[i] = element;
                }
            }
            return dummy;
        }
    
        public static int[] remove(int[] arr, int index) {
            if (arr == null || index < 0 || index >= arr.length) {
                return arr;
            }
            int[] anotherArray = new int[arr.length - 1];
            for (int i = 0, k = 0; i < arr.length; i++) {
                if (i == index) {
                    continue;
                }
                anotherArray[k++] = arr[i];
            }
            return anotherArray;
        }
    
        public static void printArraylist (ArrayList<int[]> aList) {
            for(int[] anIntArray:aList) {
                //iterate the retrieved array an print the individual elements
                for (int aNumber : anIntArray) {
                    System.out.print(aNumber+",");
                }
                System.out.println();
            }
        }
}

