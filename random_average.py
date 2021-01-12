#!/usr/bin/env python3

# created by: Ryan Walsh
# created on: January 2021
# this program calculates the average of 10 random numbers

import random


def main():
    # this program calculates the average of 10 random numbers
    my_numbers = []
    sum = 0
    for loop_counter in range(0, 10):
        random_number = random.randint(1, 100)
        my_numbers.append(random_number)

    for loop_counter in range(0, 10):
        print("The random number is {0}".format(my_numbers[loop_counter]))
        sum += my_numbers[loop_counter]
    average = sum / 10

    print("\n", end="")
    print("The average is {0}".format(average))


if __name__ == "__main__":
    main()
