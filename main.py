from Grapple_test import Container,Fish

box = Container(55,40)
box.get_water_level(10)
_ = input("push enter when fish is in")
box.add_fish(1000)

for fish in box.fish_in_box:
    fish.Calc_weight
    print(fish)