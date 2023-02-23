#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@class:       DS 2001 (Fall 2021)
@prof:        Ryan Gallagher
@author:      Alex Oswald
@date:        2021-10-18
@descr:       Practicum 06
"""

import matplotlib.pyplot as plt

BASEBALL_CSV = "lahman_batting.csv"

"""data array map
data[0]  = fname            data[7]  = H        
data[1]  = lname            data[8]  = HR       
data[2]  = year             data[9]  = SB       
data[3]  = stint            data[10] = BB       
data[4]  = team             data[11] = SO       
data[5]  = league           data[12] = HBP      
data[6]  = AB               data[13] = PA       
"""

###############  Other Functions  ###############


def read_file(file):
    """Reads and returns data from a file
    Parameters:
        file_name: str
            The name of a CSV file to read
    Returns:
        data: list of lists
            Each sublist includes the data for a row from the file
    Example
    -------
    list_of_lists_data = read_file(‘lahman_batting.csv’)
    """
    data = []
    line_list = None

    with open(file, 'r') as f:
        for line_num,line in enumerate(f):
            if line_num == 0:
                continue
            line_list = line.rstrip().split(',')

            data.append(line_list)

    return data


def filter_by_numeric(data, col_indx, min_val, max_val):
    """Description: Filters numeric data by a particular column index according 
       to whether it is within the range of a given min and max
    Parameters:
        data: list of lists
            Each sublist contains row data
        col_indx: int
            The index of the column to use
        min_val: int
            The minimum value to filter by
        max_val: int
            The maximum value to filter by
    Returns:
        filtered_data: list of lists
            Each list includes the data for a row, where the value specified by
            col_indx is between min_val and max_val
    Example
    -------
    data2000s = filter_by_numeric(data, 2, 2000, 2021)
    """
    filtered_data = []

    for i in range(len(data)):
        if min_val <= int(data[i][col_indx]) <= max_val:
            filtered_data.append(data[i])
    
    return filtered_data


def filter_by_categorical(data, col_indx, category_vals):
    """Filters categorical data (i.e. strings) by a particular column index 
       according to whether it is in a list of given values
    Parameters:
        data: list of lists
            Each sublist contains row data
        col_indx: int
            The index of the column to use
        category_vals: list of strs
            A list of strings to filter by
    Returns:
        filtered_data: list of lists
            Each list includes the data for a row, where the value specified by
            col_indx is in category_vals.
    Example
    -------
    # Data for the Boston Red Sox and Chicago White Sox
    data_sox = filter_by_categorical(data, 4, [‘BOS’, ‘CHA’])
    """
    filtered_data = []

    for i in range(len(data)):
        if data[i][col_indx] in category_vals:
            filtered_data.append(data[i])
    
    return filtered_data


def get_season_leaderboard(data, col_indx, top_n, year):
    """Gets the top players by some metric for a single season
    Parameters:
        data: list of lists
            Each sublist contains row data
        col_indx: int
            The index of the column to use
        top_n: int
            The top N players in the leaderboard
        year: int
            The year of the season
    Returns:
        leaderboard: list of lists
            Each list includes the data for a row, where each is in the top N
            for a given season according to the metric specified by col_index
    Example
    -------
    # Get the top 20 leaderboard for hits in 2018
    leaderboard = get_season_leaderboard(data, 7, 20, 2018)
    """
    YEAR_IDX = 2
    yr_filtered_data = []
    leaderboard = []

    # filter array by year
    for i in range(len(data)):
        if year == int(data[i][YEAR_IDX]):
            yr_filtered_data.append(data[i])

    # convert proper column to int
    for j in range(len(yr_filtered_data)):
        yr_filtered_data[j][col_indx] = int(yr_filtered_data[j][col_indx])

    # sort and rank by desired column
    for i in range(len(yr_filtered_data)):
        leaderboard = sorted(yr_filtered_data, key=lambda row: row[col_indx],
                             reverse=True)

    # only top N
    leaderboard = leaderboard[0:top_n]

    return leaderboard


###############  main() Function  ###############

def main():
    # 1 READING THE DATA WITH LISTS OF LISTS
    data = read_file(BASEBALL_CSV)

    # 2 FILTERING NUMERIC DATA
    # check to see if it works!
    data_check_num = filter_by_numeric(data, 2, -1, 10000)
    bool_check_num = len(data) == len(data_check_num)
    print('Lengths:', str(len(data)), 'and', str(len(data_check_num)),
          'are the same:', str(bool_check_num), '!')

    # collect 2000s data
    data_2000s = filter_by_numeric(data, 2, 2000, 2010)

    # check Ichiro Suzuki hits (in 2004 >= 262)
    data_2004 = filter_by_numeric(data, 2, 2004, 2004)
    data_2004_hits = filter_by_numeric(data, 7, 262, 1000)
    print(data_2004_hits[0][0], data_2004_hits[0][1], 'hits',
          data_2004_hits[0][7], 'times in', data_2004_hits[0][2])

    # check barry bonds walks (in 2004 >= 232)
    data_2004_walks = filter_by_numeric(data_2004, 10, 232, 1000)
    print(data_2004_walks[0][0], data_2004_walks[0][1], 'walks',
          data_2004_walks[0][10], 'times in', data_2004_walks[0][2])

    # 3 FILTERING CATEGORICAL DATA
    leagues = ['AL', 'NL']
    data_check_cat = filter_by_categorical(data, 5, leagues)
    bool_check_cat = len(data) == len(data_check_cat)
    print('Lengths:', str(len(data)), 'and', str(len(data_check_cat)),
          'are the same:', str(bool_check_cat), '!')

    # 4 SORTING AND LEADERBOARDS
    # check -> top 5 home runs in 2018
    TOP_X = 5
    HR_IDX = 8
    YEAR0 = 2018
    leaderboard_hruns = get_season_leaderboard(data, HR_IDX, TOP_X, YEAR0)

    print("\nTop", str(TOP_X), "Home Runs in", str(YEAR0) + "...")
    ct = 0
    for sublist in leaderboard_hruns:
        name = sublist[0] + ' ' + sublist[1]
        ct += 1
        print(str(ct) + '.', name + ':', str(sublist[HR_IDX]), 'home runs')

    '''Expected Output:
    Khris Davis: 48 home runs
    J. D. Martinez: 43 home runs
    Joey Gallo: 40 home runs
    Jose Ramirez: 39 home runs
    Mike Trout: 39 home runs
    '''


main()
