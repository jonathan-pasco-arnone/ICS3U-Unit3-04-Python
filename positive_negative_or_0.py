#!/usr/bin/env python3

# Created by: Jonathan Pasco-Arnone
# Created on: November 2020
# This program determines whether the number is positive, negative or 0


def main():
    # This function gets an input, determines whether the number is
    # positive, negative or 0, and then outputs the result

    print("This program determines whether a"
          "number is positive, negative or 0")
    number = int(input("Please enter a number: "))
    
    if (number == 0):
        print("The number you entered was 0")
    elif (number > 0):
        print("The number you entered was positive")
    else:
        print("The number you entered was negative")


if __name__ == "__main__":
    main()
