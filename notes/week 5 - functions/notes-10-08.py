"""
Byron Wallace + Ben Rye
DS2k lecture 8 notes

Writing Functions
"""

RUNNER = "runners.csv"


def get_sum(list_of_numbers):
    '''
    Take a parameter (list_of_numbers) which is a list of numbers, and 
    RETURN their sum
    '''
    total = 0
    for num in list_of_numbers:
        total += num

    return total



def running_fun(month_to_plot="February 2021"):
    # param = " "  -->  default param if not provided
    '''
    we want to: (1) read in the runner data for multiple months, (2) keep track 
    of the max mileage (over all months) and who achieved it

    The file looks like:

        January 2021,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,...
        Byron Wallace,3,8,0,4.5,5,4,3,0,9,0,3.25,0,4,0,3,...
        Ben Nye,0,3,0,2,0,1.5,0,0,2.5,0,2.5,0,1,1,0,3.5,0...
        February 2021...
    '''
    with open(RUNNER, 'r') as infile:
        dates = infile.readline().strip().split(",")
        month = dates.pop(0)
        
        #for date_idx in range(len(dates)):
        #    dates[date_idx] = int(dates[date_idx])
        dates = [int(date) for date in dates]

        runner1 = infile.readline().strip().split(',')
        runner1_name = runner1.pop(0)
        runner1 = [float(miles) for miles in runner1]
        print(runner1)

        runner2 = infile.readline().strip().split(',')
        runner2_name = runner2.pop(0)
        runner2 = [float(miles) for miles in runner2]
        print(runner2)
        



def sum_new_function():
    # pass makes it a placeholder and python will do nothing
    pass


running_fun()
