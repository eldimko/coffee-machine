print('Write how many cups of coffee you will need:')
cups = int(input())

water_per_cup = 200
milk_per_cup = 50
coffee_per_cup = 15

print("For {} cups of coffee you will need:".format(cups))
print("{} ml of water".format(cups * water_per_cup))
print("{} ml of milk".format(cups * milk_per_cup))
print("{} g of coffee beans".format(cups * coffee_per_cup))