
from hcsr04sensor import sensor

class fish:
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
        volume = self.water_level_change*self.lenth*self.width
        weight = self.density*volume
        self.weight = weight       




class container:
    def __init__(self,lenth,width):
        """ container class """
        self.lenth = lenth
        self.width = width
        self.fish_in_box = []
        self.water_level = 0
        
    def __repr__(self):
        return f"CONTAINER({self.lenth}*{self.width})({self.water_level})"
    
    def __str__(self):
        return f"this container has a lenth of {self.lenth}m and a width of {self.width}m and water level {self.water_level}m"
    
    def get_water_level(self,pin_in,pin_out):
        """ do this """
        mes = sensor.Measurement(pin_in,pin_out)
        
        dis = mes.raw_distance()
        return int(f"{dis:.3f}")
    
    def add_fish(self,density,water_rise):
        """ adds fish to box """
        self.water_level += water_rise
        self.fish_in_box.append(fish(water_rise,density,self.lenth,self.width))
        
        
harrys_boat = container(0.1,0.1)
print(harrys_boat)

harrys_boat.get_water_level(0.3)

harrys_boat.add_fish(1000,0.01)
for fish in harrys_boat.fish_in_box:
    fish.Calc_weight()
    print(fish)