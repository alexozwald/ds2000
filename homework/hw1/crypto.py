"""
@author:	Alex Oswald
@class:		DS2000
@homework:	Homework 1
@date:		20 September 2021
"""

# Problem 2

### TEST CASES
# Input:  1
# Output: 3e-05 Bitcoin, 2e-05 DS Coin

# Input:  100
# Output: 0.00301 Bitcoin, 0.00181 DS Coin


### Conversion Rates
# 1 Bitcoin = 33,235.00 USD
# 3/5 DS Coin = 1 Bitcoin
# DS coin is pegged to bitcoin

BTC_USD =  33235.00
BTC_DScoin = 3/5

def main():
	usd = float(input("Please enter amount in USD:  "))

	btc = usd / BTC_USD
	dscoin = btc * BTC_DScoin

	print(round(usd,2),"USD is about", round(btc,5),"Bitcoin")
	print(round(usd,2),"USD is about", round(dscoin,5),"DS Coin")

main()
