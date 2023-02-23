"""
@author:    Alex Oswald
@class:     DS2000
@homework:  Homework 3
@date:      04 October 2021
"""

'''TEST CASES
Expected from test_sorted_nums.txt:
Count:  5
Avg:    12.2
Median: 10
'''

INCOME_FILE = "sorted_income.txt"
S_NUMS_FILE = "test_sorted_nums.txt"

# Params:  string of one file in directory with 1 number/line
# Output: prints # of numbers, average, median, 
def get_data(file_name):
    # declare relevant general variables for reading + computing files
    line_ct = 0
    f_sum = 0
    avg = 0
    median = 0

    # OPEN + READ FILE
    with open(file_name, 'r') as file:
        # loop through file to read all lines.  break upon empty line.
        while True:
            # read line, strip '\n'
            line = file.readline().rstrip()
            # if not empty -> add to calculations; else -> break
            if (line != ''):
                line_ct += 1
                f_sum += int(line)
            else:
                break
    # closes file by exiting with/open

    # COMPUTE AVERAGE
    avg = f_sum / line_ct

    # COMPUTE MEDIAN
    # if line count is even
    if (line_ct % 2 == 0):
        # determine midpoint
        midpoint = int(line_ct / 2)
        # read file until midpoint+1
        with open(file_name, 'r') as file:
            for i in range(0, midpoint + 1):
                line = file.readline().rstrip()
                if (i == midpoint):
                    median = int(line)

    # if line count is odd
    elif (line_ct % 2 == 1):
        # determine midpoints
        mid_lower = int(line_ct / 2 - 0.5)
        mid_upper = int(line_ct / 2 + 0.5)
        # read file until midpoint+1
        with open(file_name, 'r') as file:
            for i in range(0, mid_upper + 1):
                line = file.readline().rstrip()
                if (i == mid_lower):
                    med_lower = int(line)
                if (i == mid_lower):
                    med_upper = int(line)    
        # calc median
        median = (med_lower + med_upper) / 2
        median = int(median)

    # RETURN ALL 3 VALUES
    return line_ct, avg, median


def main():
    # TEST CASE
    # compute through function
    test_count, test_avg, test_median = get_data(S_NUMS_FILE)

    # pretty print
    print("Expected from", S_NUMS_FILE + ":"
          "\nCount:  " + str(test_count) + 
          "\nAvg:    " + str(test_avg) + 
          "\nMedian: " + str(test_median))
    print()

    # CASE STUDY
    # compute through same process as test case
    count, avg, median = get_data(INCOME_FILE)

    # pretty print
    print("Income data from", INCOME_FILE + ":"
          "\nData points:      " + str(count) + 
          "\nAverage income:  $" + str(round(avg,2)) + 
          "\nMedian income:   $" + str(median) + ".00")


main()
