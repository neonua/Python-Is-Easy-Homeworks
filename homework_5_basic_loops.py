"""
This file describes basic work with loops
"""


def fizzbuzz():
    """
    Solution for the assignment called "Fizz Buzz"
    """
    for i in range(1, 101):
        # First chech whether number is prime or not
        if is_prime(i):
            print('prime')
            continue

        # Need this variable in order to
        # decide whether print number or not
        need_to_print_i = True

        if i % 3 == 0:
            print('Fizz', end='')
            need_to_print_i = False

        if i % 5 == 0:
            print('Buzz', end='')
            need_to_print_i = False

        if need_to_print_i:
            print(i, end='')

        # We need this print statement because we use
        # custom ending in print statements above
        print()


def is_prime(number):
    """
    Checks whether number is prime or not
    """
    list = []  # list of divisors of the number

    for i in range(1, number + 1):
        if number % i == 0:
            # If we already have more than 1 divisor we don't need
            # to append current one. Number is not prime.
            if len(list) > 1:
                return False

            list.append(i)

    # Prime number only have 2 divisors.
    # Need this check for the case of 1.
    if len(list) == 2:
        return True


# Running the function
fizzbuzz()
