"""
@author:	Alex Oswald
@class:		DS2000
@homework:	Homework 1
@date:		20 September 2021
"""

from math import floor

# Problem 4
### TEST CASES
# Input:   23 wheels, 10 frames, 1000 links
# Output:  10 bikes, 3 wheels, and 500 links leftover

# Input:   98 wheels, 55 frames, 2967 links
# Output:  49 bikes, 6 frames, 517 links



### Requirements for 1 Bike
# 2 wheels
# 1 frame
# 50 links (to make a chain)

def main():
	# user input
	wheels = int(input("How many wheels do you have?\n"))
	frames = int(input("\nHow many frames?\n"))
	links  = int(input("\nHow many links?\n"))

	# possible bikes
	most_wheels = wheels / 2
	most_frames = frames / 1
	most_links  =  links / 50

	bikes = floor(min(most_wheels, most_frames, most_links))

	# leftover parts
	leftover_wheels = wheels - (bikes * 2)
	leftover_frames = frames - (bikes * 1)
	leftover_links  =  links - (bikes * 50)
	leftover_link_chains = floor(leftover_links / 50)
	leftover_link_links  =       leftover_links % 50

	# pretty formatting (return to int type)
	bikes = int(bikes)
	leftover_wheels = int(leftover_wheels)
	leftover_frames = int(leftover_frames)
	leftover_links = int(leftover_links)
	leftover_link_chains = int(leftover_link_chains)
	leftover_link_links = int(leftover_link_links)

	# display output
	print("\nI can make you", str(bikes), "bikes with that!"
		"\nI'm keeping leftovers for myself. Which is..."
		"\n\t" + str(leftover_wheels), "wheels"
		"\n\t" + str(leftover_frames), "frames"
		"\n\t" + str(leftover_links), "links ("
		+ str(leftover_link_chains), "chains,", str(leftover_link_links), "links)")

main()
