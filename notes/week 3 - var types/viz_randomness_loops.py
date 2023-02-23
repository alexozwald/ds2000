#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Byron Wallace and Ben Nye
DS2K Lecture 4 Notes
Viz, loops, randomness
'''

'''
Let's start with some data viz!
'''

import matplotlib.pyplot as plt 

def main():
    ''' 
    Plot a point at (4, 10) with a blue "x" symbol 
    and labeled 'point 1'.
    '''
    x1 = 4
    y1 = 10
    plt.plot(x1, y1, "x", color="blue", label="point 1")
    
    ''' 
    Another at (6, 12) with a red "o" symbol 
    and labeled 'point 2'.
    '''
    x2 = 6
    y2 = 12
    plt.plot(x2, y2, "o", color="red", label="point 2")
    
    plt.legend()
    
main()

'''
Suppose now we want to plot the number of students 
in the sections of DS2K, and label them with their
session numbers
'''
def main():
    
    # Number of students per section
    n_sec_1 = 115
    n_sec_2 = 131
    n_sec_3 = 72
    
    # Make points for each section
    plt.plot(1, n_sec_1, "o", color="blue", label="Section 1")
    plt.plot(2, n_sec_2, "o", color="red", label="Section 2")
    plt.plot(3, n_sec_3, "o", color="green", label="Section 3")
    
    # Label the axes
    plt.xlabel("Section")
    plt.ylabel("Number of students")

    # Add a legend
    plt.legend() 
    

main()

'''
Let's get random! 
'''
import random 

def main():
    r = random.randint(1, 10) 

main()

'''
Coin flipping (--> conditions, loops!)
'''
def main():
    num_flips = 1
    is_heads = random.random() < 0.5
    if is_heads:
        print("Heads! After", num_flips, "tries!")
        # Tells the interpreter we’re all done here; note that 
        # this will only work with the interpreter (i.e., on the console!)
        # In any case, you don't want to use this generally.
        exit()
    
    # If we get here, we did not exit, which means we did not
    # get a heads. Need to flip again!
    num_flips = 2
    is_heads = random.random() < 0.5
    if is_heads:
        print("Heads! After", num_flips, "tries!")
        exit()
        
    # Unlucky! Let's try again
    num_flips = 3
    is_heads = random.random() < 0.5
    if is_heads:
        print("Heads! After", num_flips, "tries!")
        exit() 

    # ... Keep going until (?)
    
main()

'''
Let's try again, allowing for an arbitrary number of flips —
to accomplish this we will introduce *while loops*!
'''
def main():
    num_flips = 1
    is_heads = False
    while not is_heads:
        is_heads = random.random() < 0.5
        num_flips += 1
            
        print("Heads! After", num_flips, "tries!")
             
#main()


# BONUS: count number of heads tails seen in n flips
def main():
    '''
    Count the number of heads seen in n flips, and
    plot the number of heads and number of tails
    '''
    
    # The total number of flips to do
    num_flips = 10
    
    # Remember numer of flips we have done
    flip_counter = 0 
    # Remember the number of heads we've seen
    heads_counter = 0
    # And remember the number of tails we've seen
    tails_counter = 0
    
    # We need to simulate flipping a coin
    # 10 times and remember how many tails and
    # how many heads we saw
    while flip_counter < num_flips:
        is_heads = random.random() < 0.5
        flip_counter += 1
        if is_heads:
            heads_counter += 1
        else:
            tails_counter += 1
    
    # Now plot!
    plt.bar(1, heads_counter, label="heads")
    plt.bar(2, tails_counter, label="tails")
    plt.legend()
    plt.ylim(0, num_flips)

main()