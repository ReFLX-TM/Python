enTuCara = ""

for i in range(1,100):
    if i % 3 == 0 and i % 5 == 0:
        enTuCara += "FizzBuzz "
    
    elif i % 5 == 0:
        enTuCara += "Buzz "

    elif i % 3 == 0:
        enTuCara += "Fizz "

    else:
        enTuCara += (str(i) + " ")

print(enTuCara)