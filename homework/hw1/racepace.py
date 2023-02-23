"""
@author:	Alex Oswald
@class:		DS2000
@homework:	Homework 1
@date:		20 September 2021
"""

# Problem 3
### TEST CASES
# Input:   5k race, 0 hours, 27 minutes
# Output:  3.11 miles, 8:42 pace

# Input:   20k race, 2 hours, 05 minutes
# Output:  12.42 miles, 10:04 pace

KILO_PER_MILE = 1.61

def main():
	kilos = float(input("How many k's did you run?\n"))
	hours = int(input("\nHow many hours did it take?\n"))
	mins = int(input("\nAnd how many minutes?\n"))

	time_s = (mins * 60) + (hours * 3600)

	miles = kilos / KILO_PER_MILE
	
	pace_m = (time_s / miles) // 60
	pace_s = (time_s / miles) % 60

	print("\nCongrats on your race!  Here are your stats!")
	print("\t" + str(round(miles,2)), "miles")
	print("\t" + str(round(pace_m)) + ":" + str(round(pace_s)).zfill(2), "pace (per mile)")

main()
