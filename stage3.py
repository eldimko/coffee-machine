water_per_cup = 200
milk_per_cup = 50
beans_per_cup = 15


water_stock = int(input("Write how many ml of water the coffee machine has:"))
milk_stock = int(input("Write how many ml of milk the coffee machine has:"))
beans_stock = int(input("Write how many grams of coffee beans the coffee machine has:"))

cups = int(input("Write how many cups of coffee you will need:"))

most_water_cups = water_stock // water_per_cup
most_milk_cups = milk_stock // milk_per_cup
most_beans_cups = beans_stock // beans_per_cup

# find the smallest amount of cups out of the list in order to find the most cups of coffee that are possible to be made

most_cups_list = [most_water_cups, most_milk_cups, most_beans_cups]
most_cups_list.sort()
most_cups = most_cups_list[0]

if most_cups == cups:
    print("Yes, I can make that amount of coffee")
elif most_cups < cups:
    print("No, I can make only {} cups of coffee".format(most_cups))
elif most_cups > cups:
    print("Yes, I can make that amount of coffee (and even {} more than that)".format(most_cups - cups))
