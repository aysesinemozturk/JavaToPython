package TSP;
import java.util.ArrayList;
import java.util.Arrays;

public class enumaration{

    public static void main(String[] args) {
        
        //total number of cities that we would like to examine
        //the problem starts with 3 cities minimum
        //so 5 represents 3,4,5,6, and 7 cities at each iteraion
        double [] CPU_Time = new double[5];
        int index = 0;
        
        //it will take nodes number from 3 nodes to 7 nodes
        //At each iteration, it will store cpu time in array

        //please do not exceed 12 cities :)
        for(int i = 3; i < CPU_Time.length + 3; i++){
            long startTime = System.nanoTime();
            int[] nodeList = new int[i];
            
            for(int m = 0; m < nodeList.length; m++) {
                nodeList[m] = m;
            }
            
            
            System.out.println("--- DISTANCE MATRIX ---");
            
            //we will create random distance matrix for each iteration
            //so nodes 3 distance matrix will be different from nodes 4 distance matrix
            //therefore, shortest distance can differentiate at each iteraion
            printArraylist(candidateRoutes(nodeList), DistanceBetweenNodes(nodeList));
            
            long endTime = System.nanoTime();
            double Execution_time = ((endTime-startTime)/1000000);
            CPU_Time[index] =  Execution_time;
            index ++; 
        }
        System.out.println("---  CPU TIME ---");
        System.out.println("CPU Time of nodes from 3 to "+(CPU_Time.length+2) +": "+ Arrays.toString(CPU_Time));
        
        //End of main method
        
    }

        //random distances between each nodes, distance [i][j] = distance [j][i]
        //node i to i should be 0
        public static int[][] DistanceBetweenNodes(int[] nodeList){
            int[][] DistanceBetweenNodes = new int[nodeList.length +1][nodeList.length +1];
            
            for(int i = 0; i < nodeList.length; i++){
                System.out.print("[");
                for(int j = 0; j < nodeList.length; j++){
                    if(i == j){ //when it travels to itself
                        DistanceBetweenNodes[i][j] = 0;
                    }else if(i > j){ // in order to make same number of the same route
                        DistanceBetweenNodes[i][j] = DistanceBetweenNodes[j][i];    
                    }else{ // take random number up to 100  
                        DistanceBetweenNodes[i][j] = (int) (Math.random()*100);    
                    }    
                    
                    System.out.print(DistanceBetweenNodes[i][j] + ",");
                }
                System.out.print("]");
                System.out.println();
            }
            System.out.println();
            return DistanceBetweenNodes;    
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
    
        public static void printArraylist (ArrayList<int[]> aList, int[][] DistanceBetweenNodes) {
            
            //we will store total distance of each possible routes
            int [] DistArr = new int[aList.size()];
            int k = 0;
            
            for(int[] anIntArray:aList) {
                //iterate the retrieved array an print the individual elements
                int distance = 0;
                for(int i = 0; i< anIntArray.length; i++){
                    System.out.print(anIntArray[i] + ",");
                    if(i < anIntArray.length -1){
                        //calculating distance 
                        distance += DistanceBetweenNodes[anIntArray[i]][anIntArray[i+1]];  
                    }else if( i == anIntArray.length - 1){
                        //calculating total ditance of the solution
                        distance += DistanceBetweenNodes[anIntArray[i]][anIntArray[0]];
                    }
                    
                }
                System.out.println(); 
                System.out.println("Total Distance: " + distance);
                System.out.println();
                
                //store distances
                DistArr[k] = distance;
                k++;
            }
            
            System.out.println("--- ALL POSSIBLE ROUTES --- \n");
            //we want to see all possible solutions' distance in order to find the minimum one
            System.out.println(Arrays.toString(DistArr));
            
            //in order to compare how number of possible routes increase exponentially,
            //we calculate all possible routes at each iteration
            System.out.println("\n--- SOLUTION REPORT ---");
            System.out.println("The total number of possible routes: " + DistArr.length);
            
            //find min in distance array 
            Arrays.sort(DistArr); 
            System.out.println("The shortest distance in the problem: " + DistArr[0]);
            System.out.println();
        }
}

