#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 12:46:34 2021

@author: alexozwald
"""

name = input("What's your name?\n")
print("Hi", name + "!")

# option 1
year = input("What's your school year?\n")
print("\n" + name,"is a",year,"year college student :)")

# option 2
print("Your name is",name+". You're a",year,"year college student.")
"""
 You'd begin to run into problems using a , (comma) between the inserted name
 and the period. Commans used in print insert a space. + (plus) symbols don't.
"""