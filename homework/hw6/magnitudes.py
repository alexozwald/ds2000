"""
@author:    Alex Oswald
@class:     DS2000
@homework:  Homework 6
@date:      30 October 2021 (extended from 2021-10-25)
"""

# PROBLEM 3

import csv
import matplotlib.pyplot as plt

CSV_FILE = "earthquake_data.csv"
LOW_RANGE = [0.0, 2.9]      # [low, high)
MID_RANGE = [3.0, 4.0]      # [low, high)
HIGH_RANGE = [4.0, 10.0]    # [low, high]


def read_csv(filename):
    """Summary
    
    Args:
        filename (string): string of filename
    
    Returns:
        list: [time, latitude, longitude, depth (float), mag (float), magType]
    """
    # open csv file
    with open(CSV_FILE, 'r') as f:
        # open csv reader (from module)
        reader = csv.reader(f, delimiter=',')
        # skip header
        header = next(reader)

        data = []
        # read in rows 0:5 -> time,latitude,longitude,depth,mag,magType
        for row in reader:
            # ignore lat/long
            # time, magType = strings
            # depth, magnitude = float
            data_row = row[0:3] + [float(row[3]), float(row[4]), row[5]]
            data.append(data_row)

    return data


def filter_data(data, low, high):
    """returns months of all 
    
    Args:
        data (list): full data list separated by csv
        low (int): quake magnitude: low-end range
        high (int): quake magnitude: high-end range
    
    Returns:
        list: list of # of quakes by month within mag range
    """
    mag_data = []

    # find amt of earthquakes in each month
    for month in range(12):
        mag_data.append(0)
        for i in data:
            i_range = low <= i[4] < high
            i_month = int(i[0][5:7]) == (month + 1)
            if i_range and i_month:
                mag_data[month] += 1

    return mag_data


def plot_quakes(data_low, data_med, data_high):
    """plots earthquake data.  3 bars per month by magnitude and # of occurences
    
    Args:
        data_low (list): list of # of quakes per month within mag range - low
        data_med (list): list of # of quakes per month within mag range - med
        data_high (list): list of # of quakes per month within mag range - high
    
    Raises:
        Exception: lists arent all the same lenght
    """
    if not (len(data_low) == len(data_med) == len(data_high)):
        raise Exception("data error - input lists are not all same len")


    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep",
              "Oct", "Nov", "Dec"]
    
    # set x locations for 1/3rd bars
    width = 0.85 / 3
    x_0 = list(range(1,13))
    x_1 = list(range(1,13))
    x_2 = list(range(1,13))

    x_0 = [x - width for x in x_0]
    x_2 = [x + width for x in x_2]

    # set figure + axis
    f, ax = plt.subplots()

    # implement bar graph ()
    rect0 = ax.bar(x_0, data_low, width, label='Low Magnitude', color='#C1FFD7')
    rect1 = ax.bar(x_1, data_med, width, label='Mid Magnitude', color='#FCFFA6')
    rect2 = ax.bar(x_2, data_high, width, label='High Magnitude', color='#CAB8FF')

    # label barcolumns
    #ax.bar_label(rect0, padding=3)
    #ax.bar_label(rect1, padding=3)
    #ax.bar_label(rect2, padding=3)

    # label axes
    ax.set_title("2020 Earthquakes by Magnitude & Month")
    ax.set_xlabel('Months')
    ax.set_ylabel('# of Earthquakes')
    ax.set_xticks(x_1)
    ax.set_xticklabels(months)
    ax.set_xlim(0,13)
    ax.legend()
    f.tight_layout()

    # show plot
    plt.show()



if __name__ == '__main__':
    # read csv
    data = read_csv(CSV_FILE)

    # separate months by magnitude
    data_low = filter_data(data, LOW_RANGE[0], LOW_RANGE[1])
    data_med = filter_data(data, MID_RANGE[0], MID_RANGE[1])
    data_high = filter_data(data, HIGH_RANGE[0], HIGH_RANGE[1])

    # plot earthquakes by months
    plot_quakes(data_low, data_med, data_high)
