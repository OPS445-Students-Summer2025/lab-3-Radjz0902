#!/usr/bin/env python3

# Create the list called "my_list" here, not within any function defined below.
# That makes it a global object. We'll talk about that in another lab.
my_list = [100, 200, 300, 'six hundred']

def give_list():
    # Returns all items unchanged
    return my_list

def give_first_item():
    return str(my_list[0])  # Convert to string

def give_first_and_last_item():
    # Returns a new list with first and last items
    return [my_list[0], my_list[-1]]

def give_second_and_third_item():
    # Returns a new list with second and third items
    return [my_list[1], my_list[2]]

if __name__ == '__main__':
    print(give_list())
    print(give_first_item())
    print(give_first_and_last_item())
    print(give_second_and_third_item())

