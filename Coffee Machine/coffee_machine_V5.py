def display():
    print("The coffee machine has:")
    print(water, "of water")
    print(milk, "of milk")
    print(coffee, "of coffee beans")
    print(cups, "of disposable cups")
    print(money, "of money")


def buy():    
    print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")
    coffee_type = input()
    
    if coffee_type == "1":
        print(resources(250, 0, 16, 4))

    elif coffee_type == "2":
        print(resources(350, 75, 20, 7))
        
    elif coffee_type == "3":
        print(resources(200, 100, 12, 6))
    
    elif coffee_type == "back":
        pass


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


def resources(selected_water, selected_milk, selected_coffee, selected_price):
    global water
    global milk
    global coffee
    global cups

    if water < selected_water:
        return "Sorry, not enough water!"

    elif milk < selected_milk:
        return "Sorry, not enough milk!"

    elif coffee < selected_coffee:
        return "Sorry, not enough coffee!"

    elif cups == 0:
        return "Sorry, not enough cups!"

    else:
        return make_coffee(selected_water, selected_milk, selected_coffee, selected_price)


def make_coffee(selected_water, selected_milk, selected_coffee, selected_price):
    global water
    global milk
    global coffee
    global money
    global cups

    water -= selected_water
    milk -= selected_milk
    coffee -= selected_coffee
    cups -= 1
    money += selected_price

    return "I have enough resources, making you a coffee!"

water = 400
milk = 540
coffee = 120
cups = 9
money = 550

while True:
    print("Write action (buy, fill, take, remaining, exit):")

    action = input()

    if action == "buy":
        buy()

    elif action == "fill":
        fill()

    elif action == "take":
        take()

    elif action == "remaining":
        display()
    
    elif action == "exit":
        break