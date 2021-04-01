def is_prime(num):
    dividers = 0
    for i in range(2, num):
        if num % i == 0:
            dividers += 1
        else:
            continue
    if dividers > 1:
        return False
    else:
        return True


user_number = int(input())

if user_number in (1, 0):
    print("This number is not prime")

else:
    if is_prime(user_number):
        print("This number is prime")
    else:
        print("This number is not prime")