def prime_numbers(n):
    numbers = [int(x) for x in range(2, n + 1)]
    counter = 0
    for number in numbers:
        if number == int(number):
            counter = number + 1
            while counter <= n:
                if counter % number == 0:
                    numbers[counter - 2] = str(numbers[counter - 2])
                counter += 1
        else:
            continue

    return [x for x in numbers if x == int(x)]

first_number = int(input())
result = ""
number = first_number
prime_factors = []
counter = 1
prime_list = prime_numbers(number)
while number > 1:
    if number % prime_list[len(prime_list) - counter] == 0:
        number = number // prime_list[len(prime_list) - counter]
        prime_factors.append(prime_list[len(prime_list) - counter])
        counter = 1
        prime_list = prime_numbers(number)
    else:
        counter += 1

prime_factors.sort(reverse = True)
for prime in prime_factors:
    result += str(prime) + " x "

print("Prime Factors of {} are: {}".format(first_number, result).rstrip(" x "))