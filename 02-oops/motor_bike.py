# Class
class MotorBike:
    def __init__(self, speed):
        self.speed = speed #State

    # Behavior
    def increase_speed(self, how_much):
        self.speed += how_much

    # Behavior
    def decrease_speed(self, how_much):
        if(self.speed-how_much>0):
            self.speed -= how_much
        else:
            print("Get a life")


# instance 1 or object 1
honda = MotorBike(50)

# instance 2 or object 2
ducati = MotorBike(250)

# print(honda)
# print(ducati)
#

# State changes through behavior of the object
honda.increase_speed(150)
ducati.increase_speed(25)

# State changes through behavior of the object
honda.decrease_speed(50)
ducati.decrease_speed(25)

honda.decrease_speed(350)

print(honda.speed)
print(ducati.speed)

#
# honda.speed = 150
# print(honda.speed)
# print(ducati.speed)