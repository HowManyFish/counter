from Grapple_test import Container,Fish

box = Container(55,40)
box.add_sensor((24,23))
box.add_sensor((21,20))
box.add_controller()
box.get_water_level(5)
_ = input("push enter when fish is in")
box.add_fish(2700,5)

for fish in box.fish_in_box:
    fish.Calc_weight()
    print(fish)