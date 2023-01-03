#!/bin/env python3


from ast import Num


def binary_search(fulllist, num):
    midindex = round(len(fulllist) / 2)
    mid = fulllist[midindex]
    print("midindex is {}".format(midindex))
    print("mid is {}".format(mid))
    while len(fulllist) > 1:
        print("fulllist is {}".format(fulllist))
        print("len of fulllist is {}".format(len(fulllist)))
        if num < mid:
            print("{} is less than midpoint {}".format(num, mid))
            binary_search(fulllist[0:midindex], num)
        elif num > fulllist[midindex]:
            print("{} is greater than midpoint {}".format(num, mid))
            binary_search(fulllist[midindex:], num)
        elif num == fulllist[midindex]:
            print(
                "Found the number at index {} of the list {}".format(midindex, fulllist)
            )
            return num
    print("Not found")
    return


if __name__ == "__main__":
    input_string = input("Please enter your list of numbers:")
    list_input = input_string.split(" ")
    non_empty_list = list(filter(None, list_input))
    orig_list = [int(x) for x in non_empty_list]
    int_list = sorted(orig_list)
    input_search_number = input("Please enter a number to search for")
    search_number = int(input_search_number)
    binary_search(int_list, search_number)

print("Running")
