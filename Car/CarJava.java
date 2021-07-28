package Car;

public class CarJava {
  
    // Attributes
  public int numberOfPassengers;
  public double gasolineCapacity;
  public double consumptionRate;
  public int averageSpeed;
  public double distanceTravelled;  

  public CarJava(int NumberOfPassengers, double GasolineCapacity,double ConsumptionRate, int AverageSpeed,
  double DistanceTravelled){ //constructor
      numberOfPassengers = NumberOfPassengers;
      gasolineCapacity = GasolineCapacity;
      consumptionRate = ConsumptionRate;
      averageSpeed = AverageSpeed;
      distanceTravelled = DistanceTravelled;
  }

  //behaviors of car object
  //function 1: car can move in certain time period

  public void move(int hours){

    double range = gasolineCapacity / consumptionRate; //maximum distance that car can take with its remained gasoline
    double distanceToTravel = hours * averageSpeed; // distance = time * velocity

    if(range >= distanceToTravel){
        double spentGasoline = distanceTravelled * consumptionRate;
        gasolineCapacity -= spentGasoline;
        distanceTravelled += distanceToTravel;
    
    }else{
        distanceTravelled += range;
        gasolineCapacity = 0;
    }
  }

  //function 2: see outputs of car object about its move
  public void report(){
      System.out.println("distance travelled: " + distanceTravelled);
      System.out.println("remaining gasoline after travel: " + gasolineCapacity);
  }

}
