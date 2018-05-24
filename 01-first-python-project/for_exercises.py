# is_prime(9); //Is a number Prime?
# //H: 5 => True, 7 => True, 11 => True, 6 => False
def is_prime(number):

    if(number < 2):
        return False

    # check if number is divisible by 2 to number - 1
    for divisor in range(2,number):
        if number % divisor == 0:
            return False

    return True

# print(is_prime(15));

# sum_upto_n(6)
# Sum of numbers upto n?
# 1 + 2 + 3 + 4 + 5 + 6

def sum_upto_n(number):

    sum = 0

    for i in range(1, number+1):
        sum = sum + i

    return sum

# print(sum_upto_n(6))
# print(sum_upto_n(10))

def calculate_sum_of_divisors(number):
    sum = 0

    if(number < 2):
        return sum


    for divisor in range(1,number+1):
        if number % divisor == 0:
            sum = sum + divisor

    return sum

# print(calculate_sum_of_divisors(6))
# print(calculate_sum_of_divisors(15))

def print_a_number_triangle(number):
    for j in range(1, number + 1):
        for i in range(1, j + 1):
            print(i, end=' ')
        print()


print_a_number_triangle(6)