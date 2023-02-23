#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Byron Wallace
DS2k lecture 2021/11/09

Classes & Object-Orientation
"""

import requests
import matplotlib.pyplot as plt

#from movie import movie
from tmdbv3api import Movie

# api key
API_KEY = "d1ea292bbf429bfdd03b23f6925dac09"

def search_movie(api_key, query):
	http_params = {"api_key": api_key, "query": query}
	response = requests.get("https://api.themoviedb.org/3/search/movie", params=http_params)
	return response.json()["results"]


def search_year(api_key, year, max_pages=5):
	page = 1
	data = []

	while page < max_pages:
		http_params = {"api_key": api_key,
					   "primary_release_year": year,
					   "page": page}
		response = requests.get("https://api.themoviedb.org/3/search/movie", params=http_params)
		page += 1
		data += response.json()["results"]


if __name__ == '__main__':
	print(search_movie(API_KEY, "star wars"))

	...

	pass

