# Write your code here
def display():
    print("The coffee machine has:")
    print(water, "of water")
    print(milk, "of milk")
    print(coffee, "of coffee beans")
    print(cups, "of disposable cups")
    print(money, "of money")

def buy():
    global cups
    
    print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")
    coffee_type = input()
    
    if coffee_type == "1":
        make_coffee(250, 0, 16, 4)
        
    elif coffee_type == "2":
        make_coffee(350, 75, 20, 7)
        
    elif coffee_type == "3":
        make_coffee(200, 100, 12, 6)
    
    cups -= 1

#
#
#
def fill():
    global water
    global milk
    global coffee
    global cups
    
    print("Write how many ml of water do you want to add:")
    water += int(input())
    
    print("Write how many ml of milk do you want to add:")
    milk += int(input())
    
    print("Write how many grams of coffee beans do you want to add:")
    coffee += int(input())
    
    print("Write how many disposable cups of coffee do you want to add:")
    cups += int(input())

def take():
    global money
    print("I gave you", "$" + str(money))
    money = 0

def make_coffee(selected_water, selected_milk, selected_coffee, selected_price):
    global water
    global milk
    global coffee
    global money

    water -= selected_water
    milk -= selected_milk
    coffee -= selected_coffee
    money += selected_price


water = 400
milk = 540
coffee = 120
cups = 9
money = 550

display()
print("Write action (buy, fill, take):")

action = input()

if action == "buy":
    buy()

elif action == "fill":
    fill()
    
elif action == "take":
    take()

display()