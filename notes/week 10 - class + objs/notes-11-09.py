#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Byron Wallace
DS2k lecture 2021/11/09

Classes & Object-Orientation
"""

#default
class ClassName(object):
	"""docstring for ClassName"""
	def __init__(self, arg):
		super(ClassName, self).__init__()
		self.arg = arg
		

class Car:

	def __init__(self,name,year,price):
		print("hello!")
		self.name = name
		self.year = year
		self.price = price
		#pass

	def vroom(self):
		print(self.name, "vroom!")



another_car = Car("toyota", 2002, 600)
the_tesla = Car("tesla", 2019, 200000)
another_car.vroom()

# class names are ALWAYS capitalized

import random
from matplotlib import pyplot as plt

VALID_SUITS = {1:"\u2663", 2:"\u2666", 3:"\u2665", 4:"\u2660"}
FACE_CARDS = {1:"Ace", 11:"Jack", 12:"Queen", 13:"King"}

class Card:

	def __init__(self, suit=4, value=1):
		self.suit = suit
		self.value = value
		print(self)

	def __str__(self):
		card = str(self.value)
		if self.value in FACE_CARDS:
			card = FACE_CARDS[self.value]
		card += " " + VALID_SUITS[self.suit]

		return card

class Deck:
	"""
	A representation of a deck of cards
	"""

	def __init__(self, num_values=13, num_suits=4):
		self.num_cards = num_values * num_suits
		self.cards = []
		self.make_deck(num_values, num_suits)

	def make_deck(self, num_values, num_suits):
		for val in range(1, num_values+1):
			for suit in range(1, num_suits+1):
				self.cards.append(Card(suit, val))

	def draw(self):
		if not self.cards:
			return None
		c = self.cards.pop(0)
		self.cards.append(c)
		return c

	def shuffle(self):
		"""
		mix up order of cards
		"""
		for i in range(len(self.cards)):
			#swap every card with another card position randomly chosen
			r = random.randint(0, self.num_cards-1)
			self.cards[i], self.cards[r] = self.cards[r], self.cards[i]


#my_52 = Deck()





def war():
	# initialize a deck
	d = Deck()
	d.shuffle()

	#play a game of war
	points = [0, 0]
	while points[0] < 10 and points[1] < 10:
		card_1 = d.draw()
		card_2 = d.draw()
		print(card_1, "vs", card_2)

		winner = 0
		if card_2.value > card_1.value:
			winner = 1

		points[winner] += 1
		print("Player", winner+1, "wins this round!")



if __name__ == "__main__":
	war()

