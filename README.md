# coffee-machine
Entry level python assignment from JetBrains Academy


## About

What can be better than a cup of coffee during a break? A coffee that you don’t have to make yourself. It’s enough to press a couple of buttons on the machine and you get a cup of energy; but first, we should teach the machine how to do it. In this project, you will work on programming a coffee machine simulator. The machine works with typical products: coffee, milk, sugar, and plastic cups; if it runs out of something, it shows a notification. You can get three types of coffee: espresso, cappuccino, and latte. Since nothing’s for free, it also collects the money.

## Learning outcomes

This project allows you to get a taste of Python. Practice working with functions, challenge yourself with loops and conditions, and get more confident in Python.

# Objectives per stage

## Stage 1

Write a program that puts basic information on the screen: give the machine a chance to tell the customers what it’s doing!

The first version of the program just makes you a coffee. It should print to the standard output what it is doing as it makes the drink.

## Stage 2

Program the machine to calculate the amount of ingredients it needs depending on how many people want some coffee.

Let's break the task into several steps:

1. First, read the numbers of coffee drinks from the input.

2. Figure out how much of each ingredient the machine will need. Note that one cup of coffee made on this coffee machine contains 200 ml of water, 50 ml of milk, and 15 g of coffee beans.

3. Output the required ingredient amounts back to the user.

## Stage 3

Working with conditions, program the machine to estimate how many creamy coffees it can make based on the amount of ingredients we enter.


Write a program that does the following:

1. It requests the amounts of water, milk, and coffee beans available at the moment, and then asks for the number of cups a user needs.
2. If the coffee machine has enough supplies to make the specified amount of coffee, the program should print "Yes, I can make that amount of coffee".
3. If the coffee machine can make more than that, the program should output "Yes, I can make that amount of coffee (and even N more than that)", where N is the number of additional cups of coffee that the coffee machine can make.
4. If the amount of given resources is not enough to make the specified amount of coffee, the program should output "No, I can make only N cups of coffee".

Like in the previous stage, the coffee machine needs 200 ml of water, 50 ml of milk, and 15 g of coffee beans to make one cup of coffee.


## Stage 4

Upgrade your knowledge of functions – set the machine to perform three basic actions: collect the money, renew the supplies, and serve the coffee.

Write a program that offers to buy one cup of coffee or to fill the supplies or to take its money out. Note that the program is supposed to do one of the mentioned actions at a time. It should also calculate how many ingredients and money have left. Display the number of supplies before and after purchase.

1. First, your program reads one option from the standard input, which can be "buy", "fill", "take". If a user wants to buy some coffee, the input is "buy". If a special worker thinks that it is time to fill out all the supplies for the coffee machine, the input line will be "fill". If another special worker decides that it is time to take out the money from the coffee machine, you'll get the input "take".
2. If the user writes "buy" then they must choose one of three types of coffee that the coffee machine can make: espresso, latte, or cappuccino.
For one espresso, the coffee machine needs 250 ml of water and 16 g of coffee beans. It costs $4.
For a latte, the coffee machine needs 350 ml of water, 75 ml of milk, and 20 g of coffee beans. It costs $7.
And for a cappuccino, the coffee machine needs 200 ml of water, 100 ml of milk, and 12 g of coffee. It costs $6.
3. If the user writes "fill", the program should ask them how much water, milk, coffee and how many disposable cups they want to add into the coffee machine.
4. If the user writes "take" the program should give all the money that it earned from selling coffee.

At the moment, the coffee machine has $550, 400 ml of water, 540 ml of milk, 120 g of coffee beans, and 9 disposable cups.

## Stage 5

Program the machine to display on the screen the amount of supplies left. Set the main loop: now the menu keeps updating until you enter “exit”.

Write a program that will work endlessly to make coffee for all interested persons until the shutdown signal is given. Introduce two new options: "remaining" and "exit".

Do not forget that you can be out of resources for making coffee. If the coffee machine doesn't have enough resources to make coffee, the program should output a message that says it can't make a cup of coffee.

And the last improvement to the program at this step — if the user types "buy" to buy a cup of coffee and then changes his mind, they should be able to type "back" to return into the main cycle.

## Stage 6

Your final task is to refactor the program. Make it so that you can communicate with the coffee machine through a single method. Good luck!

Time for some final touch-ups: structure the code so that it runs smoothly.

# References

JetBrains Academy: https://hyperskill.org/

Tic-Tac-Toe project link: https://hyperskill.org/projects/68?track=2