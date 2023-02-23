"""
@author:    Alex Oswald
@class:     DS2000
@homework:  Homework 2
@date:      27 September 2021
"""

import matplotlib.pyplot as plt

def main():
    #################################
    ##          Problem 1          ##
    #################################
    # Test Cases
    # The average of x-coordinates is: 85.0
    # The average of y-coordinates is: 73.7

    # read home info
    with open("home.txt", 'r') as datafile:
        x_home = int(datafile.readline())
        y_home = int(datafile.readline())
        color_home = datafile.readline()

    # read dunkin info
    with open("dunks.txt", 'r') as datafile:
        x_dnkn = int(datafile.readline())
        y_dnkn = int(datafile.readline())
        color_dnkn = datafile.readline()

    # read starabucks info
    with open("starbucks.txt", 'r') as datafile:
        x_sbux = int(datafile.readline())
        y_sbux = int(datafile.readline())
        color_sbux = datafile.readline()

    # calculate averages
    x_avg = (x_home + x_dnkn + x_sbux) / 3
    y_avg = (y_home + y_dnkn + y_sbux) / 3

    # print results
    print("The average of x-coordinates is:", str(round(x_avg,1)))
    print("The average of y-coordinates is:", str(round(y_avg,1)))
    print()

    #################################
    ##          Problem 2          ##
    #################################
    # Test Cases
    # House to Dunkin’ (Euclidean):   55.08
    # House to Starbucks (Euclidean): 48.37
    # Closer location (Euclidean): Starbucks (48.374 units)

    # calc euclidean distances
    euclid_dnkn = ( (x_home - x_dnkn)**2 + (y_home - y_dnkn)**2 )**0.5
    euclid_sbux = ( (x_home - x_sbux)**2 + (y_home - y_sbux)**2 )**0.5

    # print results, find closer store
    print("House to Dunkin’ (Euclidean):  ", str(round(euclid_dnkn,2)))
    print("House to Starbucks (Euclidean):", str(round(euclid_sbux,2)))
    if (min(euclid_dnkn, euclid_sbux) == euclid_dnkn):
        print("Closer location (Euclidean): Dunkin' (" + str(round(euclid_dnkn,3)) + ")")
    else:
        print("Closer location (Euclidean): Starbucks (" + str(round(euclid_sbux,3)) + ")")
    print()

    #################################
    ##          Problem 3          ##
    #################################
    # Test Cases
    # House to Dunkin’ (Manhattan):   58
    # House to Starbucks (Manhattan): 66
    # Closer location (Manhattan): Dunkin' (58 units)


    # calc manhattan distances
    manhattan_dnkn = abs(x_home - x_dnkn) + abs(y_home - y_dnkn)
    manhattan_sbux = abs(x_home - x_sbux) + abs(y_home - y_sbux)

    # print results, find closer store
    print("House to Dunkin’ (Manhattan):  ", str(manhattan_dnkn))
    print("House to Starbucks (Manhattan):", str(manhattan_sbux))
    if (min(manhattan_dnkn, manhattan_sbux) == manhattan_dnkn):
        print("Closer location (Manhattan): Dunkin' (" + str(manhattan_dnkn) + ")")
    else:
        print("Closer location (Manhattan): Starbucks (" + str(manhattan_sbux) + ")")
    print()

    #################################
    ##          Problem 4          ##
    #################################
    # Test Cases [visual]
    
    plt.plot(x_home, y_home, "o", color = color_home, label = "Home ⌂")
    plt.plot(x_dnkn, y_dnkn, "o", color = color_dnkn, label = "Dunkin'")
    plt.plot(x_sbux, y_sbux, "o", color = color_sbux, label = "Starbucks")
    plt.title("Local Coffee Places & Home")
    plt.legend()


main()
