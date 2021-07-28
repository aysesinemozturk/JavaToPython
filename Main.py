from CarPython import CarPython

# car objects
Car1 = CarPython(5,120,0.01,100,0)
Car2 = CarPython(4,120,0.05,120,0)

# in order to see how the performance of car objects based on different travel hours.
print('------- CAR1 PERFORMANCE -------')
for i in range(1,5):
    print("TRAVEL PERIOD: {} HOUR(S)".format(i))
    Car1.move(i)
    Car1.report()
   
print('------- CAR2 PERFORMANCE -------')
for i in range(1,5):
     print("TRAVEL PERIOD: {} HOUR(S)".format(i))
     Car2.move(i)
     Car2.report()
