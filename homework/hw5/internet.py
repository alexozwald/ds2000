"""
@author:    Alex Oswald
@class:     DS2000
@homework:  Homework 5
@date:      18 October 2021
"""

import csv

DATAFILE = "internet_access.csv"


# Reads the CSV file in and return one row of data as a list of strings
def read_csv(file, x):
    count = 0

    # open file for codeblock
    with open(file, 'r') as f:
        #read ALL lines in file
        csv_reader = csv.reader(f, delimiter=',')

        # loop through each row
        for row in csv_reader:
            if x == count:
                str_list = row
                break
            count += 1
            

    # pop row name
    str_list.pop(0)

    return str_list


# Converts a list of strings to a list of ints
def convert_to_int(str_list):
    # remove all commas
    temp_list = [y.replace(',', '') for y in str_list]

    # convert each str in list to int
    int_list = [int(x) for x in temp_list]

    return int_list


# Computes a percentage of one item in a list compared to another
def pct_of_total(int_list, col_total, col_compare):
    numerator = int_list[col_compare]
    denominator = int_list[col_total]

    pct = numerator / denominator * 100

    return pct


###  test_internet_access.py PASSED!  ###


# main function
if __name__ == "__main__":
    '''Chosen Question:
    What percent of all students rarely have access to a device for
    educational purposes?
    '''
    descr = read_csv(DATAFILE, 5)
    totals_row = convert_to_int(read_csv(DATAFILE, 7))

    rare_access = pct_of_total(totals_row, 0, 4)

    # pretty print question + results
    question = "What percent of all students rarely have access to a device for educational purposes?"
    percent = str(round(rare_access,2)) + '%'
    descr_rare = descr[4]

    print(question)
    print(percent, "of all students have a device", descr_rare[7:])




