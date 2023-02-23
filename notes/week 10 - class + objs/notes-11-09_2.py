#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Byron Wallace
DS2k lecture 2021/11/09

Classes & Object-Orientation
"""

from card_objects import Card, Deck, Player

def war():
	#initialize a deck
	d = Deck()
	...

def war2:
	d = Deck()
	d.shuffle()

	player_name - input("what is your name? ")
	player_1 = Player(player_name, is_computer=False)
	player_2 = Player("Hal", is_computer=True)

	while player_1.points < 10 and player_2.points < 10:
		prompt_str = "Your turn {}. Press d to draw.".format(player_1.player_name)
		key = input(prompt_str)
		if key == "d":
			card_1 = d.draw()
			card_2 = d.draw()

			print(card_1, "vs", card_2)

			# super pythonic of us
			winner = player_1 if card_1 > card_2 else player_2

			winner.points += 1

			player_1 = print_points()
			player_2 = print_points()


if __name__ == "__main__":
	war2()
