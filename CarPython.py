class CarPython:
    
    def __init__(self, NumberOfPassangers, GasolineCapacity,ConsumptionRate, AverageSpeed, DistanceTravelled):
        # constructor of python
        self.numberOfPassangers = NumberOfPassangers
        self.gasolineCapacity = GasolineCapacity
        self.consumptionRate = ConsumptionRate
        self.averageSpeed = AverageSpeed
        self.distanceTravelled = DistanceTravelled
    
    # behaviours of car object, function1: car can move
    
    def move(self,hours):

        maxTravel = self.gasolineCapacity / self.consumptionRate
        distanceToTravel = hours * self.averageSpeed
        
        if(maxTravel >= distanceToTravel):
            spentGasoline = self.distanceTravelled * self.consumptionRate
            self.gasolineCapacity -= spentGasoline
            self.distanceTravelled += distanceToTravel
        else:
            self.distanceTravelled = distanceToTravel
            self.gasolineCapacity = 0
    
    def report(self):
        print("Distance travelled: ", self.distanceTravelled)
        print("Remaining gasoline capacity: ", self.gasolineCapacity)



    
