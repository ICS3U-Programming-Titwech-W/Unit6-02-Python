#!/usr/bin/env python3

# Created by: Titwech Wal
# Created on: May.30.2022
# program genertate numbers, puts them
# into a list then displays it

import constants
import random


def max_value(rand_num):

    max = rand_num[0]

    # calculate the max value
    for counter in range(len(rand_num)):
        if max < rand_num[counter]:
            max = rand_num[counter]
    return max


def main():

    # initlizing sum and counter
    counter = 0
    sum = 0

    # declaring empty list
    list_of_num = []

    for counter in range(constants.MAX_SIZE):
        list_of_num.append(random.randint
                           (constants.MIN_NUM, constants.MAX_NUM))

        sum = sum + list_of_num[counter]
        print("{} is added to the list at position {}"
              . format(list_of_num[counter], counter))

    max_user = max_value(list_of_num)
    print("")
    print("The max value is: {}" .format(max_user))


if __name__ == "__main__":
    main()
