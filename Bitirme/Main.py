from Trucks import Trucks
from Bunker_Line import Bunker_Line
from QC_Area import QC_Area

ExecutionTime = 500
TotalTone = 25
InitialWaste = 1
InitialSmall = 1.25
Alim = 1400
Satis = 8000
SmallSatis = 400
WastSatis = 100
Coef = 0.0145


Truck1 = Trucks(1,0,0,0,0,0,0,0,0,0,0,0)
Truck2 = Trucks(2,2,0,0,0,0,0,0,0,0,0,0)
Truck3 = Trucks(3,39,0,0,0,0,0,0,0,0,0,0)
Truck4 = Trucks(4,57,0,0,0,0,0,0,0,0,0,0)
Truck5 = Trucks(5,60,0,0,0,0,0,0,0,0,0,0)
Truck6 = Trucks(6,62,0,0,0,0,0,0,0,0,0,0)
Truck7 = Trucks(7,93,0,0,0,0,0,0,0,0,0,0)
Truck8 = Trucks(8,132,0,0,0,0,0,0,0,0,0,0)
Truck9 = Trucks(9,165,0,0,0,0,0,0,0,0,0,0)
Truck10 = Trucks(10,192,0,0,0,0,0,0,0,0,0,0)

trucks_array = []
trucks_array.append(Truck1)
trucks_array.append(Truck2)
trucks_array.append(Truck3)
trucks_array.append(Truck4)
trucks_array.append(Truck5)
trucks_array.append(Truck6)
trucks_array.append(Truck7)
trucks_array.append(Truck8)
trucks_array.append(Truck9)
trucks_array.append(Truck10)

QC_Area1 = QC_Area(1,20, 127, "idle", 0)
Bunker_Line1 = Bunker_Line(1,120, 8300, "idle",0)
Bunker_Line2= Bunker_Line(2,120, 8300, "idle",0)
Bunker_array = []
Bunker_array.append(Bunker_Line1)
Bunker_array.append(Bunker_Line2)

TotalCost = 0

for time in range(0,ExecutionTime):
    
    for obj in trucks_array:

        
        if(obj.Arrival_Time <= time):
           
            
            if(obj.QC_Check == 0):
                
                if(QC_Area1.Idleness == "idle"):
                    
                    obj.QC_Check = 1
                    
                    obj.QC_StartTime = time
                    obj.QC_FinishTime = time + QC_Area1.WorkingTime
                    
                    print
                    print("THE QC PROCESS HAS BEEN STARTED")
                    print ("time: {}".format(time))
                    print("truck index: {}".format(obj.index))
                    print ("QC Start Time: {}".format(obj.QC_StartTime))
                    print("QC Finish Time: {}".format(obj.QC_FinishTime))
                    print
                    
                else:
                    QC_Area1.TotalTime += 1
                    
            else:
                if(time < obj.QC_FinishTime):
                    QC_Area1.Idleness = "busy"
                
                elif(time == obj.QC_FinishTime):
                    QC_Area1.Idleness = "idle"
                    print("QC area is idle right now")
                    print
            
            if(obj.BL_Check == 0 and obj.QC_Check == 1 and time >= obj.QC_FinishTime):  
                for b_number in Bunker_array:  
                        if(b_number.Idleness == "idle" and obj.BL_Check == 0):
                                
                                obj.BL_Check = 1
                                b_number.Idleness == "busy"
                                obj.BL_StartTime = time
                                obj.BL_FinishTime = time + Bunker_Line1.WorkingTime
                                
                                print("time: {}".format(time))
                                print("truck index: {}".format(obj.index))
                                print ("BL Start Time: {}".format(obj.BL_StartTime))
                                print("BL Finish Time: {}".format(obj.BL_FinishTime))
                                print
                                
                                if(obj.QC_Check == 1 and obj.BL_Check == 1):
                                        
                                        print("END TİME: {}".format(time))
                                        print("truck index: {}".format(obj.index))
                                 
                                        obj.Waiting_Time = (obj.QC_StartTime - obj.Arrival_Time) + (obj.BL_StartTime - obj.QC_FinishTime)
                                        obj.Wasted_Potato = InitialWaste + (TotalTone - InitialWaste)*Coef*obj.Waiting_Time
                        
                                        print ("Wasted Potato: {}".format(obj.Wasted_Potato))
                                        print ("Waiting Time: {}".format(obj.Waiting_Time))
                        else:
                            b_number.TotalTime += 1
                else:
                    
                    if(time < obj.BL_FinishTime):
                        b_number.Idleness = "busy"
                
                    elif(time == obj.BL_FinishTime):
                        b_number.Idleness = "idle"
       
           
                



                

                        




            






