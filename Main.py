from CarPython import CarPython

# car objects
Car1 = CarPython(5,120,0.01,100,0)
Car2 = CarPython(4,120,0.05,120,0)

# in order to see how the performance of car objects based on different travel hours.
for i in range(1,5):
    Car1.move(i)
    Car1.report
    Car2.move(i)
    Car2.report
