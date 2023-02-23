"""
@author:	Alex Oswald
@class:		DS2000
@homework:	Homework 1
@date:		20 September 2021
"""

# Problem 1

### TEST CASES
# Input:	12 years
# Output:	144 months, 4380 days, 105120 hours

# Input:	19 years
# Output:	228 months, 6935 days, 166440 hours


MONTH_CONV = 12
DAY_CONV = 365
HOUR_CONV = 8760

def main():
	years = int(input("Enter your age (years):  "))

	months = years*MONTH_CONV
	days = years*DAY_CONV
	hours = years*HOUR_CONV

	print(years,"years is...")
	print("\t" + str(months), "months")
	print("\t" + str(days), "days")
	print("\t" + str(hours), "hours")

main()
