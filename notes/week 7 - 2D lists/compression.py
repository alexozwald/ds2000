#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 12:26:42 2021

@author: byronwallace
"""
import csv 
import matplotlib.pyplot as plt

def decompress(lst):
    ''' Function: decompress
        Parameters: list of strings with the format:
                    [x, s, x, s] where the x indicates the number of "s"
                    to put into a new list
        Returns: a list of strings, the uncompressed list
    '''
    uncompressed = []
    for i in range(0, len(lst), 2):
        for j in range(int(lst[i])):
            uncompressed.append(lst[i + 1])
    return uncompressed


def plot_compressed(filename, size = .1):
    ''' Function: plot_compressed
        Parameters: filename, a string, and size of each square, an int
        Returns: nothing, just renders a plot
    '''
    with open(filename) as csvfile:      
        csv_reader = csv.reader(csvfile, delimiter = ",")
        y = 0
        for row in csv_reader:        
            uncomp = decompress(row)
            x = 0
            for color in uncomp:
                plt.plot(x, y, "s", color = color, markersize = size * 1.5)
                x += size
            y -= size

IMG1 = "compressed.csv"
IMG2 = "compressed2.csv"

if __name__ == "__main__":
    num = int(input("Which img do you want to decompress, 1 or 2?\n"))
    if num == 1:
        plot_compressed(IMG1, 10)
    else:
        plot_compressed(IMG2, 5)
