
from hcsr04sensor import sensor
from ultrasonic_sensor import Sensor
from Displacement_calc import MeasurementController

class Fish:
    def __init__(self,water_level_change,density,lenth_of_box,width_of_box):
        """ fish class """
        self.water_level_change = water_level_change
        self.weight = 0
        self.lenth = lenth_of_box
        self.width = width_of_box
        self.density = density
        
    def __repr__(self):
        return f"Fish(weight,{self.weight})"
    
    def __str__(self):
        return f"this is a fish of weight {self.weight}"
    
    def Calc_weight(self):
        """ clculates weight of fish with box peramiters and density of fish """
        print(f"water_level_change,{self.water_level_change}")
        print(f"length,{self.lenth}")
        print(f"width,{self.width}")
        volume = self.water_level_change*self.lenth*self.width
        print(f"volume,{volume}")
        print(f"density,{self.density}")
        weight = self.density*volume
        print(f"weight,{weight}")
        self.weight = weight       




class Container:
    def __init__(self,lenth,width):
        """ container class """
        self.lenth = lenth
        self.width = width
        self.fish_in_box = []
        self.water_level = 0
        self.sensors = []
        self.measurment = None
        self.calabrated_level = 0.0
        self.weight = 0.0

    def __repr__(self):
        return f"CONTAINER({self.lenth}*{self.width})({self.water_level})"
    
    def __str__(self):
        return f"this container has a lenth of {self.lenth}m and a width of {self.width}m and water level {self.water_level}m"
    
    def get_water_level(self,rounds: int):
        """ do this """
        mes,_ = self.measurment.gattling_gun(rounds)
        self.water_level= mes

    def zero_sensor(self,rounds):
        self.get_water_level(rounds)
        self.calabrated_level = self.water_level
        
    
    def add_fish(self,density,rounds:int):
        """ adds fish to box """
        level_before = self.water_level
        self.get_water_level(rounds)
        level_after = self.water_level
        water_rise = (level_before - level_after) * 0.01
        self.fish_in_box.append(Fish(water_rise,density,self.lenth,self.width))
        
    def add_sensor(self,pins: tuple):
        self.sensors.append(Sensor(pins))
        
    def add_controller(self):
        self.measurment = MeasurementController(self.sensors)

    def total_weight(self,rounds):
        self.get_water_level(rounds)
        change = (self.water_level - self.calabrated_level)/100
        a = Fish(change,1000,self.lenth,self.width,)
        a.Calc_weight()
        self.weight = a.weight