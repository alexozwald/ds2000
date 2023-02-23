#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Byron Wallace and Ben Nye
DS2K Lecture 10 Notes

More on functions: Revisiting calculating distances (as in HW2)
"""

import matplotlib.pyplot as plt 

DUNKS = "all_dunks.txt"

def read_file(filename):
    ''' Function: read_file
        Parameter: filename, a string
        Returns: a list of ints from the file
        Does: Assumes one value per line, everything is an int
    '''
    data = []
    with open(filename, "r") as infile:
        for line in infile:
            data.append(int(line))
    return data

def euclidean(x1, y1, x2, y2):
    ''' Calculate the Euclidean distance b/w (x1, y1) and (x2, y2)
        Parameters: four ints/floats repping two points
        Returns: a float, euclidean distance between the points
    '''
    x_diff = (x2 - x1) ** 2
    y_diff = (y2 - y1) ** 2
    dist = (x_diff + y_diff) ** 0.5
    return dist


def manhattan(x1, y1, x2, y2):
    ''' Calculate the Manhattan distance b/w (x1, y1) and (x2, y2)
        Parameters: four ints/floats, repping two points
        Returns: a float, the manhattan distance between the points
    '''
    x_diff = abs(x2 - x1)
    y_diff = abs(y2 - y1)
    dist = x_diff + y_diff
    return dist

def find_closest(x, y, all_points, distance):
    ''' Function: find_closest
        Parameters: x and y (int/float) repping one point, a list of
                    points to compare to, and a distance function
        Returns: a float, the smallest distance of them all
        Does: calls the distance function on the given x, y against all points 
              in the list, assuming the list has structure [x, y, x, y, ...]
    '''
    min_dist = distance(x, y, all_points[0], all_points[1])
    min_x = all_points[0]
    min_y = all_points[1]
    for i in range(2, len(all_points), 2):
        dist = distance(x, y, all_points[i], all_points[i + 1])
        if dist < min_dist:
            min_dist = dist
            min_x = all_points[i]
            min_y = all_points[i + 1]
    return [min_dist, min_x, min_y]


def main():
    
    # Collect data -- home (x, y) point comes from the user,
    # and all the coffee points come from a file
    home_x = int(input("What is your x-coord?\n"))
    home_y = int(input("What is your y-coord\n"))
    points = read_file(DUNKS)

    # Calculations -- find the closest coffee to home,
    # using manhattan and euclidean distance
    close_euc = find_closest(home_x, home_y, points, euclidean)
    close_hat = find_closest(home_x, home_y, points, manhattan)

    # Report results -- give the closest distance
    print("Using Euclidean distance, the closest coffee to you is...\n"
          "\t", close_euc[0], "away!")
    print("Using Manhattan distance, the closest coffee to you is...\n"
          "\t", close_hat[0], "away!")

    # Report results -- for visualizations, plot all the points
    # and then plot home and the closest coffee on their own
    for i in range(0, len(points), 2):
        plt.plot(points[i], points[i + 1], ".", color = "orange")
        
    plt.plot(home_x, home_y, "s", color = "red", label = "home")
    plt.plot(close_euc[1], close_euc[2], 
             "o", color = "black", label = "nearest neighbor")
    plt.legend(loc="upper right")

main()

