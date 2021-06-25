# class Car:

#     def init(self,name,gear,miles):
#         self.name = name
#         self.gear = gear
#         self.miles = miles

#     def drive(self,miles):
#         self.miles = self.miles + miles

#     def shift_gear(self, gear):
#         self.gear = gear
# car = Car("tesla", 0,0)
# car.shift_gear(6)      
# print(car.gear) 
class Robot:
    def __init__(self, name, speed, job):
        self.name = name
        self.speed = speed
        self.job = job

    def clean_room(self, time, distance):
        self.distance = time / self.speed

car = Robot("Toyota", 5, "engineer")
car.clean_room(233, 0)
print(car.time)   