"""
@author:    Alex Oswald
@class:     DS2000
@homework:  Homework 3
@date:      04 October 2021
"""

import matplotlib.pyplot as plt

'''ADDITIONAL QUESTION
The data in the file comes from the US Census Bureau, but of course it’s only a 
small snippet of the entire country. What could be the dangers involved in 
drawing conclusions about the stats (average, median) we’ve gathered here?

By drawing conclusions about the stats from this data, you'd be extrapolating a 
small sample set (996 pts) to a significantly larger population (329.5 million).
As irresposible as it would be to draw conclusions from such a small data set, 
you also risk classifying the country into a smaller subset of groups than would
be appropriate if geography and other socioeconomic factors were considered.
'''

HH_INCOME = "hh_income.txt"


# function to clean up color selection
def colorpick(num):
    # income bracket -> color & shape
    if (num > 150000):
        color = '#5C4B51'
        shape = 'p'
    elif (90000 <= num < 150000):
        color = '#8CBEB2'
        shape = '*'
    elif (57500 <= num < 90000):
        color = '#F2EBBF'
        shape = '*'
    elif (25000 <= num < 57500):
        color = '#F3B562'
        shape = '.'
    elif (num < 25000):
        color = '#F06060'
        shape = '.'
    
    return color, shape


def main():
    # open file
    with open(HH_INCOME, 'r') as file:
        i = 0
        # loop until empty line (EOF)
        while True:
            # read line to string
            line = file.readline().rstrip('\n')
            i += 1

            if (line != ''):
                # determine vars, incl color/shape in other func for readability
                x = i
                y = int(line)
                hue, shape = colorpick(y)

                # plot point
                plot = plt.scatter(x, y, color=hue, marker=shape)
            else:
                break

    # final plot tweaks
    plt.title("Income Distribution")
    plt.xlabel("Position in " + HH_INCOME)
    plt.ylabel("Income ($)")
    #plt.legend(title="Brackets", markerscale=3)

    # display plot
    plt.show()


main()
