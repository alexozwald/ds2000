#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@class:       DS 2001 (Fall 2021)
@prof:        Ryan Gallagher
@author:      Alex Oswald
@date:        2021-09-29
@descr:       Practicum 04
"""

import matplotlib.pyplot as plt
from numpy import percentile
from math import floor, sin, cos, asin

# constants
RADIUS = 3959.87433


def main():
    # 1 READING IN TRIP DURATIONS

    # variable declarations (incl. file name)
    data = []
    line = ''
    line_list = []
    datafile = "2021-08_bluebike_6924.csv"
    # datafile parasing lists & parameters
    durations = []      # line_list[0] = duration (s)
    start_station = []  # line_list[1] = station name, start
    start_lat = []  # line_list[2] = latitude, start
    start_lon = []  # line_list[3] = longitude, start
    end_station = []    # line_list[4] = station name, end
    end_lat = []    # line_list[5] = latitude, end
    end_lon = []    # line_list[6] = longitude, end
    sub_type = []       # line_list[7] = subscriber type


    # read csv file
    with open(datafile, 'r') as file:
        while True:
            # read + process lines
            line = file.readline().rstrip()
            line_list = line.split(',')

            # if EOF, else parse data
            if (line != ''):
                durations.append(int(line_list[0]))
                start_station.append(line_list[1])
                start_lat.append(float(line_list[2]))
                start_lon.append(float(line_list[3]))
                end_station.append(line_list[4])
                end_lat.append(float(line_list[5]))
                end_lon.append(float(line_list[6]))
                sub_type.append(line_list[7])

                # 2D data array:  data[line][data type]
                data.append(line_list)
            else:
                break

    # 2 SUBSCRIBERS AND CUSTOMERS
    duration_subs = []
    duration_cust = []

    # loop over full dataset. check for subscriber/customer status
    # --> add data[x][0] (duration) to appropriate list
    for i in range(0,len(data)):
        if (data[i-1][7] == 'Subscriber'):
            temp = int(data[i-1][0])
            duration_subs.append(temp)
        elif (data[i-1][7] == 'Customer'):
            temp = int(data[i-1][0])
            duration_cust.append(temp)

    # fastest + longest trips
    subs_min_time = min(duration_subs)
    subs_max_time = max(duration_subs)
    subs_avg_time = sum(duration_subs[0:len(duration_subs)]) / len(duration_subs)
    
    cust_min_time = min(duration_cust)
    cust_max_time = max(duration_cust)
    cust_avg_time = sum(duration_cust[0:len(duration_cust)]) / len(duration_cust)

    # format for readability
    subs_min_time_mins = str(floor(subs_min_time / 60))
    subs_min_time_secs = str(subs_min_time % 60).zfill(2)

    subs_max_time_mins = str(floor(subs_max_time / 60))
    subs_max_time_secs = str(subs_max_time % 60).zfill(2)

    subs_avg_time_mins = str(floor(subs_avg_time / 60))
    subs_avg_time_secs = str(int(subs_avg_time % 60)).zfill(2)

    cust_min_time_mins = str(floor(cust_min_time / 60))
    cust_min_time_secs = str(cust_min_time % 60).zfill(2)

    cust_max_time_mins = str(floor(cust_max_time / 60))
    cust_max_time_secs = str(cust_max_time % 60).zfill(2)

    cust_avg_time_mins = str(floor(cust_avg_time / 60))
    cust_avg_time_secs = str(int(cust_avg_time % 60)).zfill(2)

    # print data
    print("The average trip duration for Subscribers was",
          subs_avg_time_mins + ':' + subs_avg_time_secs)
    print("The shortest trip was", subs_min_time_mins + ':' + subs_min_time_secs +
          ", and the longest trip was", subs_max_time_mins + ':' + subs_max_time_secs)
    print()
    print("The average trip duration for Customers was",
          cust_avg_time_mins + ':' + cust_avg_time_secs)
    print("The shortest trip was", cust_min_time_mins + ':' + cust_min_time_secs +
          ", and the longest trip was", cust_max_time_mins + ':' + cust_max_time_secs)
    print()

    # BoxPlots with matplotlib.  Added breakplot for extreme min/max outliers
    fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True, 
                                   gridspec_kw={'height_ratios': [1, 8]})
    fig.subplots_adjust(hspace=0.05)  # adjust space between axes

    # limit each axis
    ax1.set_ylim(max(durations) - 100, max(durations) + 100)  # outliers only
    ax2.set_ylim(0, percentile(durations, 99))   # most of the data

    # hide the spines between ax1 and ax2
    ax1.spines.bottom.set_visible(False)
    ax2.spines.top.set_visible(False)
    ax1.xaxis.tick_top()
    ax1.tick_params(labeltop=False)  # don't put tick labels at the top
    ax2.xaxis.tick_bottom()

    # make slanted lines between subplot breaks
    d = .25  # proportion of vertical to horizontal extent of the slanted line
    kwargs = dict(marker=[(-1, -d), (1, d)], markersize=12,
                  linestyle="none", color='k', mec='k', mew=1, clip_on=False)
    ax1.plot([0, 1], [0, 0], transform=ax1.transAxes, **kwargs)
    ax2.plot([0, 1], [1, 1], transform=ax2.transAxes, **kwargs)

    # simplify data for boxplot + extreme plotting funcs
    bp_duration = [durations, duration_subs, duration_cust]
    extremes = [[min(durations), max(durations)],
                [min(duration_subs), max(duration_subs)],
                [min(duration_cust), max(duration_cust)]]

    # print boxplot on lower subplot
    ax2.boxplot(bp_duration, positions=[1,2,3], widths=0.6, whis=(5,95),
                showfliers=False)
    # print extremes on both subplots
    ax1.scatter([[1,1],[2,2],[3,3]], extremes, marker='x', color='red')
    ax2.scatter([[1,1],[2,2],[3,3]], extremes, marker='x', color='red')

    # label plots & figure appropriately
    fig.suptitle("Durations of Bluebike Rentals")
    plt.xticks([1,2,3], ['All', 'Subscribers', 'Customers'])
    plt.ylabel("Minutes")
    #plt.show() -> moved to end of fn
    print("NOTE: Plot will open last.\n")

    # 3 TRIP DISTANCES AND SPEEDS
    #speed = distance / time
    distance = []
    dist_subs = []
    dist_cust = []
    speed_subs = []
    speed_cust = []
    for i in range(0, len(sub_type)):
        d = 2 * RADIUS * asin( sin((end_lat[i] - start_lat[i]) / 2)**2 + 
            cos(start_lat[i]) * cos(end_lat[i]) * sin((end_lon[i] - start_lon[i]) / 2)**2 )
        distance.append(d)

    # separate all distances per subscriber -- in line with duration_* lists
    for i in range(0, len(distance)):
        if (sub_type[i] == 'Subscriber'):
            dist_subs.append(distance[i])
        elif (sub_type[i] == 'Customer'):
            dist_cust.append(distance[i])
        else:
            print("error on " + str(i))

    # calculate speed (subscribers)
    for i in range(0, len(dist_subs)):
        temp_speed = (dist_subs[i] / duration_subs[i])
        speed_subs.append(temp_speed)

    # calculate speed (customers)
    for i in range(0, len(dist_cust)):
        temp_speed = (dist_cust[i] / duration_cust[i])
        speed_cust.append(temp_speed)


    # get statistics by type
    subs_min_speed = min(duration_subs)
    subs_max_speed = max(duration_subs)
    subs_avg_speed = sum(duration_subs[0:len(duration_subs)]) / len(duration_subs)
    
    cust_min_speed = min(duration_cust)
    cust_max_speed = max(duration_cust)
    cust_avg_speed = sum(duration_cust[0:len(duration_cust)]) / len(duration_cust)

    # format for readability
    subs_min_speed_mins = floor(subs_min_speed / 60)
    subs_min_speed_secs = str(int(subs_min_speed % 60)).zfill(2)
    subs_min_speed_str = str(subs_min_speed_mins) + ':' + subs_min_speed_secs

    subs_max_speed_mins = floor(subs_max_speed / 60)
    subs_max_speed_secs = str(int(subs_max_speed % 60)).zfill(2)
    subs_max_speed_str = str(subs_max_speed_mins) + ':' + subs_max_speed_secs

    subs_avg_speed_mins = floor(subs_avg_speed / 60)
    subs_avg_speed_secs = str(int(subs_avg_speed % 60)).zfill(2)
    subs_avg_speed_str = str(subs_avg_speed_mins) + ':' + subs_avg_speed_secs

    cust_min_speed_mins = floor(cust_min_speed / 60)
    cust_min_speed_secs = str(int(cust_min_speed % 60)).zfill(2)
    cust_min_speed_str = str(cust_min_speed_mins) + ':' + cust_min_speed_secs

    cust_max_speed_mins = floor(cust_max_speed / 60)
    cust_max_speed_secs = str(int(cust_max_speed % 60)).zfill(2)
    cust_max_speed_str = str(cust_max_speed_mins) + ':' + cust_max_speed_secs

    cust_avg_speed_mins = floor(cust_avg_speed / 60)
    cust_avg_speed_secs = str(int(cust_avg_speed % 60)).zfill(2)
    cust_avg_speed_str = str(cust_avg_speed_mins) + ':' + cust_avg_speed_secs

    # print speed statistics
    print("The average trip duration for Subscribers was", subs_avg_speed_str)
    print("The shortest trip was", subs_min_speed_str +
          ", and the longest trip was", subs_max_speed_str)
    print()
    print("The average trip duration for Subscribers was", cust_avg_speed_str)
    print("The shortest trip was", cust_min_speed_str +
          ", and the longest trip was", cust_max_speed_str)
    print()

    plt.show()


main()