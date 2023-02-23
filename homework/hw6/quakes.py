"""
@author:    Alex Oswald
@class:     DS2000
@homework:  Homework 6
@date:      30 October 2021 (extended from 2021-10-25)

Attributes:
    CSV_FILE (str): Description
"""

# PROBLEM 2

import csv
import matplotlib.pyplot as plt
import matplotlib.colors
import matplotlib.cm

CSV_FILE = "earthquake_data.csv"



def read_csv_dates(filename):
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


def separate_months(data):
    """separates months from complex time string

    Args:
        data (list): data read in from csv
    
    Returns:
        list: 1D list of all months (ints) earthquakes occurred in 2020 (sorted)
    """
    months_list = []
    for row in data:
        curr_month = int(row[0][5:7])
        months_list.append(curr_month)

    return months_list


def plot_quake_dates(months_list):
    """plots earthquake data in bar graphs for each month by # of occurences
    
    Args:
        months_list (list): list of months (ints) earthquakes occurred in 2020.
    """
    months = ["January", "February", "March", "April", "May", "June", "July",
              "August", "September", "October", "November", "December"]
    month_idx = list(range(1,13))
    print(month_idx)

    # find amt of earthquakes in each month
    month_sums = [0] * len(month_idx)
    for month in range(len(month_idx)):
        for month_item in months_list:
            if (month_item == month_idx[month]):
                month_sums[month] += 1

    print(month_sums)

    # set figure + axis
    f, ax = plt.subplots()

    # COLOR GEN 1
    # make diff bars rainbow - choose rainbow colormap
    cmap = matplotlib.cm.get_cmap('Pastel2')
    cmap2 = matplotlib.cm.get_cmap('Set2')

    # COLOR GEN 2
    # get diff rainbow - not a qualitative colormap
    clist, elist = [], []
    #normalize item number values to colormap
    norm = matplotlib.colors.Normalize(vmin=min(month_sums), vmax=max(month_sums))
    for i in range(len(month_idx)):
        #colormap possible values = viridis, jet, spectral
        rgba_color = matplotlib.cm.cool(norm(month_sums[i]))
        clist.append(rgba_color)

    # implement bar graph
    ax.bar(month_idx, month_sums, width=0.85, color=cmap.colors, edgecolor=cmap2.colors)
    #ax.bar(month_idx, month_sums, width=0.85, color=clist, edgecolor=elist)


    # label axes
    ax.set_title("2020 Earthquakes")
    ax.set_xlabel('Months')
    ax.set_ylabel('# of Earthquakes')
    ax.set_xticks(month_idx)
    ax.set_xticklabels(months, rotation=30)
    plt.tight_layout()

    # show plot
    plt.show()



if __name__ == '__main__':
    # read csv
    data = read_csv_dates(CSV_FILE)
    # separate months
    months_list = separate_months(data)
    # plot earthquakes by months
    plot_quake_dates(months_list)
