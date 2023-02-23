#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 14:16:41 2021

@author: alexozwald
"""

import math

# constants
CAR_CAPACITY = 400 #lbs
BIKE_CAPACITY = 100 #lbs
AVERAGE_POTATO_LBS = 0.38 #lbs


## 1 How Many Potatoes?
volunteers = int(input("[1] How many volunteers are available?  "))

car_lbs = CAR_CAPACITY * volunteers
bike_lbs = BIKE_CAPACITY * volunteers

print("[1] If they have cars, your", volunteers, "volunteers can rescue", car_lbs, "lbs of potatoes!")
print("[1] If they have bicycles, your", volunteers, "volunteers can rescue", bike_lbs, "lbs of potatoes!")

car_potato = float(car_lbs)/AVERAGE_POTATO_LBS
bike_potato = float(bike_lbs)/AVERAGE_POTATO_LBS

print("[1] If they have cars, your", volunteers, "volunteers can rescue", car_potato, "potatoes!")
print("[1] If they have bicycles, your", volunteers, "volunteers can rescue", bike_potato, "potatoes!")


## 2 Recommending Volunteers
store = input("[2] What's the name of the grocery store?  ")
str_lbs_input = "[2] How many pounds of potatoes does " + store + " have to pick up?  "
lbs_input = float(input(str_lbs_input))

store_volunteers_car = lbs_input / CAR_CAPACITY
store_volunteers_bike = lbs_input / BIKE_CAPACITY

print("[2] If they have cars, you need", store_volunteers_car, "volunteers!")
print("[2] If they have bicycles, you need", store_volunteers_bike, "volunteers!")

## 3 No Partial Volunteers
store_volunteers_car_floor = math.floor(store_volunteers_car)
store_volunteers_bike_floor = math.floor(store_volunteers_bike)

print("[3] If they have cars, you need", store_volunteers_car_floor, "volunteers!")
print("[3] If they have bicycles, you need", store_volunteers_bike_floor, "volunteers!")

## 4 Using Constants
# see top of document

## 5 Submit Your Work
"""
I didn't have any paarticular troubles completing the assignment.  Thank you
for your patience!
-Alex
"""