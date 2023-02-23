#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Byron Wallace and Ben Nye
DS2K Lecture 6 Notes
Looping, conditionals, and lists!

As usual, these examples are for instructive purposes,
and do not always represent ideally commented/documented
code! 
"""

'''
First, a new way of ending loops!
'''

# Looping the "old" way
# while <condition>:
#   <do stuff>
counter = 1
while counter < 5:
    print(counter)
    counter += 1
    
print("")

# Can also use *break* (although this is not a great candidate for it)
counter = 1
while True: 
    print(counter)
    counter += 1
    if counter >= 5:
        break
    
'''
Introducing: Lists!
'''
# a list of ints
a_list_of_ints = [1,2,3]
# a list of strings
a_list_of_strings = ["a", "b", "c"]
# a list of strings and ints!
a_mixed_list = ["a", "b", "c", 1, 2, 3]
# an empty list
an_empty_list = []

###
# Can append items, remove items!
a_list = []
a_list.append(3)
a_list.append("hi")
print(a_list)
# access a specific element
print(a_list[1])
# remove the first element
a_list.pop(0)


# Iterate over lists!
some_numbers = [1,2,3,4,5,6,7,8]

for num in some_numbers:
    print(num)

# A bit more interesting...
for num in some_numbers:
    if num % 2 == 0:
        print("even!")
    else:
        print("odd!")
    

'''
OK, let's say we want to write some code to iterate over lists until we hit a
particular element.
'''

def main():
    a_list = ["x", 3, 4, -3, "stop", 1000, "buffy"]
    stop_at = "stop"
    
    cur_idx = 0
    cur_element = None
    # One way of doing this
    '''
    while cur_element != "stop":
        cur_element = a_list[cur_idx]
        # Q: Will this print "stop" ever?
        print(cur_element)
        cur_idx += 1
    '''
    
    # A nicer way
    for element in a_list:
        if element == "stop":
            break
    print(element)


#main()

'''
Now let's modify this to build up another list such that it contains all 
elements up to but excluding "stop"
'''
def main():
    a_list = ["x", 3, 4, -3, "stop", 1000, "buffy"]
    stop_at = "stop"
    
    new_list = []
    
    for element in a_list:
        if element == "stop":
            break
        new_list.append(element)
    print(new_list)

main()

'''
*Removing all* elements and adding to our new list
'''
def main():
    a_list = ["x", 3, 4, -3, "stop", 1000, "buffy"]
    
    new_list = []
    # Note! In general having a condition that involves 
    # a variable you are modifying is not really good 
    # practice
    while len(a_list) > 0:
        new_list.append(a_list.pop(0))
        
    print("original list", a_list)
    print("new list", new_list)

main()


'''
    DS2000
    Fall 2021
    Sample code from class -- using a while loop to read from a file
'''

DUNKS_FILE = "all_dunks.txt"

def main():
    # Initialize variables to zero to track the total sum of x values,
    # total sum of y values, and total number of numbers in the file
    total_x = 0
    total_y = 0
    count = 0
    
    # Open the file and read until we hit the end
    # Read two lines at a time, one for x-coord and one for y-coord
    infile = open(DUNKS_FILE, "r")
    while True:
        x_line = infile.readline()
        y_line = infile.readline()
        if x_line == "" or y_line == "":
		   # We did something similar with our Buffy transcript example!
           break
       
       	# Once we know we've read in legit values,
       	# add on to the totals we're tracking
       	x_coord = int(x_line)
       	y_coord = int(y_line)
       	total_x += x_coord
       	total_y += y_coord
        count += 1
           
 	# We're at the end of the file, report results
    avg_x = total_x / count
    avg_y = total_y / count
    print("We read", count, "total (x, y) pairs, and we've found\n"
        "\t avg x-coord...", round(avg_x, 3), "\n"
        "\t avg y-coord...", round(avg_y, 3))

#main()    

import matplot.pyplot as plt
def main():
    '''
    Assemble *list of coordinates, plot them all!
    '''
    list_of_coordinates = []
    
    in_file = open(DUNKS_FILE, "r")
    
    while True:
        x_coord = in_file.readline()
        y_coord = in_file.readline()
        
        if x_coord == "" or y_coord == "":
            break
        
        x_coord = int(x_coord)
        y_coord = int(y_coord)
        
        # Create a new list that contains
        # the current x coordinate and y coordinate
        x_and_y = [x_coord, y_coord]
        
        list_of_coordinates.append(x_and_y)
    
    in_file.close()
    
    num_dunks = len(list_of_coordinates)
    print("Number of dunks:", num_dunks)
    print(list_of_coordinates)
    
    ###
    # Given a list of coordinates, plot them!
    for coordinate in list_of_coordinates:
        plt.plot(coordinate[0], coordinate[1], 'o')
    
main()




