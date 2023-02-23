"""
@author:    Alex Oswald
@class:     DS2000
@homework:  Homework 6
@date:      30 October 2021 (extended from 2021-10-25)
"""

# PROBLEM 1

import csv
import matplotlib.pyplot as plt

CSV_FILE = "positions.csv"


def read_csv(filename):
    # open csv file
    with open(CSV_FILE, 'r') as f:
        # open csv reader (from module)
        reader = csv.reader(f, delimiter=',')
        # recursively read 2D list of *ints*
        data = [[int(x) for x in row] for row in reader]
    
    return data


def square_nodes(x, y):
    # four points of the square
    x_list = [x, x,   x+1, x+1]
    y_list = [y, y+1, y+1, y]

    return x_list, y_list


def make_qr():
    data = read_csv(CSV_FILE)

    # height = row of file
    for y in range(0, len(data)):
        # x coordinate = from csv list
        for x in data[y]:
            #plt.plot(x, y, 's', color='black', markersize=8)
            sq_x, sq_y = square_nodes(x, y)
            plt.fill(sq_x, sq_y, color='black')

    # set axes + preserve aspect ratio
    plt.ylim = (0, len(data))
    plt.xlim = (0, len(data))
    plt.axis('equal')

    # preserve aspect ratio
    plt.title("QR Code")

    plt.show()


make_qr()
# qr linked url:
# https://course.ccs.neu.edu/ds2000sp21/code/hw6/important_link.html
