def tax_calculator(value):
    global percentage
    
    if value <= 15527:
        return 0
    elif value <= 42707:
        percentage = 15
        return round(value * (percentage / 100))
    elif value <= 132406:
        percentage = 25
        return round(value * (percentage / 100))
    else:
        percentage = 28
        return round(value * (percentage / 100))


income = input()
percentage = 0
tax = tax_calculator(int(income))
print("The tax for {} is {}%. That is {} dollars!".format(income, percentage, tax))