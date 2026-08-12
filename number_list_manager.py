# Warm-up program 1
# Build a menu-based program that manages a list of random numbers.
# This file is meant to warm you up before the larger student system.
# Try to handle errors by using if-statements or try-except blocks.
# Show a menu for the user that gives the following choices:

# 1. Show all data in the list (NOTE: YOU SHOULD NOT JUST PRINT THE ENTIRE LIST, e.g., print(my_list) is wrong)
# 2. Sort the list in ascending order
# 3. Sort the list in descending order
# 4. Add a number
# 5. Remove a specific number
# 6. Remove the last number
# 7. Remove the first number
# 8. Sum all numbers

# You should try to use separate functions for each functionality.

# Starting code

import random

def random_numbers():
    return random.randrange(1,7)

def random_numbers_list():
    numbers = []
    count = 0
    while count < 10:
        numbers.append(random_numbers())
        count += 1
    return numbers

def show_data(numbers):
    if not numbers:
        print("This number does not exist in this list")
        return
    print("\nList of content:")
    i = 0
    while i < len(numbers):
        print(i+1, ": ", numbers[i])
        i += 1


numbers = random_numbers_list()
print("This program contains a list of 10 random numbers between 1 and 6")
    
while True:
    print("1. Show all data in the list")
    print("2. Sort the list in asceding order")
    print("3. Sort the list in descending order")
    print("4. Add a number")
    print("5. Remove a specific number")
    print("6. Remove the last number")
    print("7. Remove the first number")
    print("8. Sum all numbers")
    print("9. Exit program")

    choice = input("\nEnter your choice (1-9):")

    if choice == "1":
        show_data(numbers)
    elif choice == "2":
        numbers.sort()
        print("listed sorted in ascending order.")
    elif choice == "3":
        numbers.sort(reverse=True)
        print("List sorted in descending order")
    elif choice == "4":
        try:
            num = int(input("Enter a number to add:"))
            numbers.append(num)
            print(num, "added")
        except:
            print("Error: Please eneter a valid number.")
    elif choice == "5":
        try:
            num = int(input("Enter a number to remove"))
            if num in numbers:
                numbers.remove(num)
                print(num, "had been removed")
            else:
                print("Number not found")
        except:
            print("Error: Enter a valid number")
    elif choice == "6":
        if not numbers:
            print("The list is empty")
        else:
            numbers.pop()
            print("Last element has been removed")
            print("New complete list", show_data(numbers))
    elif choice == "7":
        if not numbers:
            print("The list is empty")
        else:
            numbers.pop(0)
            print("The first element has been removed")
            print("This is the new complete list", show_data(numbers))
    elif choice == "8":
        print("Sum of all the numbers", sum(numbers))
    elif choice == "9":
        print("You have exited the program")
        break
    else:
        print("You have enverd an invalid choice")





        