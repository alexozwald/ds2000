#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@class:       DS 2001 (Fall 2021)
@prof:        Ryan Gallagher
@author:      Alex Oswald
@date:        2021-09-24
@descr:       Practicum 03
"""

import matplotlib.pyplot as plt

    #################################################
    ##         1 Reading Demographic Data          ##
    #################################################

def main():
    # intro to program
    print("Boston neighborhoods with available data:"
          "\nAllston, Backbay, Dorchester, Fenway, HarborIslands, JamaicaPlain,"
          "Longwood, Roslindale, and Roxbury.")

    # get input
    place = input("\nWhat neighborhood would you like to know about? ")

    # read requested data
    with open(place.lower()+".txt", 'r') as datafile:
        size = float(datafile.readline())
        population = int(datafile.readline())
        median_age = int(datafile.readline())

    # prettyprint output
    print('\n' + place.title(), "is", str(size), "sq mi large, has", 
       str(population), "and the median age is", str(median_age), "years old.")

    '''QUESTION 1
    What are two things that a user might do to accidentally cause your program to 
    encounter an error?

    Potential faults in this program include the case that users use may not use 
    lowercase letters, spell something wrong and not be able to redo it, not know 
    what neighborhoods they can request info from, among others.

    To account for this, I altered how the strings were used to predetermine how 
    case would function throughout the programa independent of the users input.
    '''

    #################################################
    ##          x Comparing Demographics           ##
    #################################################

    # get input
    place1 = input("Please input a 1st neighborhood:  ")
    place2 = input("Please input a 2nd neighborhood:  ")
    place3 = input("Please input a 3rd neighborhood:  ")
    
    print("\n(comparison types:  size, population, median_age)")
    compare = input("What demographic do you want to compare?  ")
    
    # The final output would then be a plot of the populations of Fenway,
    # Roxbury, and Dorchester
    
    # read all data
    with open(place1.lower()+".txt", 'r') as datafile1:
        size1 = float(datafile1.readline())
        population1 = int(datafile1.readline())
        median_age1 = int(datafile1.readline())

    with open(place2.lower()+".txt", 'r') as datafile2:
        size2 = float(datafile2.readline())
        population2 = int(datafile2.readline())
        median_age2 = int(datafile2.readline())

    with open(place3.lower()+".txt", 'r') as datafile3:
        size3 = float(datafile3.readline())
        population3 = int(datafile3.readline())
        median_age3 = int(datafile3.readline())
    
    # sort data & separate requested data
    places = [place1.title(), place2.title(), place3.title()]

    sizes = [size1, size2, size3]
    populations = [population1, population2, population3]
    median_ages = [median_age1, median_age2, median_age3]

    if (compare.lower() == "size"):
        bar_heights = sizes
    elif (compare.lower() == "population"):
        bar_heights = populations
    elif (compare.lower() == "median_age"):
        bar_heights = median_ages
    else:
        print("There was an error with your input.")

    # plot data
    plt.bar(places, bar_heights)
    plt.ylabel(compare.title())
    plt.title("Comparison of Neighborhoods")

    #################################################
    ##            3 Ideal Neighborhoods            ##
    #################################################

    # get input (ideals)
    ideal_size = float(input("What is the geographic size of your ideal neighborhood?  "))
    ideal_population = int(input("What is the population size of your ideal neighborhood?  "))
    ideal_median_age = int(input("What is the median age in your ideal neighborhood?  "))

    # USING DATA FROM PART 1
    # size comparison
    if (abs(ideal_size - size) <= 0.25):
        print(place.title(), "fits your size criteria.")
        ideal1 = True;
    else:
        print(place.title(), "does not fit your size criteria.")
        ideal1 = False

    # population comparison
    if (abs(ideal_population - population) <= 3000):
        print(place.title(), "fits your population criteria.")
        ideal2 = True
    else:
        print(place.title(), "does not fit your population criteria.")
        ideal2 = False

    # median age comparison
    if (abs(ideal_median_age - median_age <= 4)):
        print(place.title(), "fits your age criteria.")
        ideal3 = True
    else:
        print(place.title(), "does not fit your age criteria.")
        ideal3 = False

    # overall comparison
    if (ideal1 or ideal2 or ideal3):
        print(place.title(), "is an OK match.")
    else:
        print(place.title(), "is a bad match.")

    #################################################
    ##               x Finish Early?               ##
    #################################################

main()
