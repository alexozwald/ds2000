'''
    DS2000
    Fall 2021
    HW5 - Testing all the functions
'''

from internet import read_csv, convert_to_int, pct_of_total

TESTFILE = "test.csv"
EPSILON = 0.001

def test_read_csv(filename, row, expected):
    ''' Function: test_read_csv
        Parameters: a string for filename, an int for row,
                    and a list of strings for what we expect
        Returns: boolean indicating if the test passed
    '''
    actual = read_csv(filename, row)
    print("In read CSV...\n",
          "\tExpected:", expected, "\n",
          "\tActual:", actual)
    return actual == expected

def test_convert_to_int(lst, expected):
    ''' Function: test_convert_to_int
        Parameters: List of strings, list of ints (expected result)
        Returns: boolean indicating if test passed
    '''
    actual = convert_to_int(lst)
    print("In convert to int...\n",
          "\tExpected:", expected, "\n",
          "\tActual:", actual)
    return actual == expected

def test_pct_of_total(lst, total, col, expected):
    ''' Function: test_pct_of_total
        Parameters: List of ints, total and col (ints), and expected result
        Returns: boolean indicating if test passed
    '''
    actual = pct_of_total(lst, total, col)
    print("In convert to int...\n",
          "\tExpected:", expected, "\n",
          "\tActual:", actual)
    return abs(actual - expected) < EPSILON

    
if __name__ == "__main__":
    
    #
    # Test the CSV read function
    #
    print(".........Testing CSV Function..........")
    num_fail = 0
    if not test_read_csv(TESTFILE, 0, ["100", "25", "50"]):
        num_fail += 1
    if not test_read_csv(TESTFILE, 1, ['1,000', '250', '500']):
        num_fail += 1
    if num_fail == 0:
        print("All CSV tests passed, congrats!")
    else:
        print(num_fail, "tests broke in CSV read function, pls fix :(")
        
    #
    # Test the Convert to int function
    #
    print("\n\n\n\n\n.........Testing Convert to Int Function..........")
    num_fail = 0
    if not test_convert_to_int(["1", "23", "456"], [1, 23, 456]):
        num_fail += 1
    if not test_convert_to_int(["1,001", "2,4,5,6", "10,10,10,01"], 
                               [1001, 2456, 10101001]):
        num_fail += 1
    if num_fail == 0:
        print("All conversion tests passed, congrats!")
    else:
        print(num_fail, "conversion tests failed, pls fix :(")
        
    #
    # Test the percent of total function
    #
    print("\n\n\n\n\n.........Testing Pct of Total Function..........")
    num_fail = 0
    if not test_pct_of_total([27, 25], 0, 1, 92.5925):
        num_fail += 1
    if not test_pct_of_total([1000, 4455, 6397], 0, 2, 639.7):
        num_fail += 1
    if num_fail == 0:
        print("All percent tests passed, congrats!")
    else:
        print(num_fail, "percent tests failed, pls fix :(")
        
        