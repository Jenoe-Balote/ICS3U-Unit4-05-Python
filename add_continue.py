#!/usr/bin/env python3

# Created by: Jenoe Balote
# Created on: May 2019
# This program determines the sum of positive numbers
#   inputted by the user


def main():
    # this function runs the "Add Continue" program

    # input
    string_to_add = str(input("How many numbers do you want to add?: "))
    print("")

    # process & output
    try:
        integer_to_add = int(string_to_add)
        loop_counter = 0
        total = 0
        if integer_to_add > 0:
            while integer_to_add > loop_counter:
                num_string = str(input("Enter a number to add: "))
                try:
                    num_integer = int(num_string)
                    loop_counter += 1
                    if num_integer < 0:
                        continue
                    total += num_integer
                except Exception:
                    print("Invalid number!")
                    continue
            print("The sum of all positive numbers is {}.".format(total))
        else:
            print("Invalid number!")
    except Exception:
        print("{} is not an integer at all!".format(string_to_add))
    finally:
        print("")
        print("Thanks for participating!")


if __name__ == "__main__":
    main()
