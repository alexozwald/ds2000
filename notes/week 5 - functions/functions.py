#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Byron Wallace and Ben Nye
DS2K Lecture 8 Notes

Writing functions
"""

'''
Write something to accept a string and print out a (naive) phonetic
pronounciation.
'''
PRONOUNCE_FILE = "pronunciation.txt"

def pronounce_v1():
    '''
    Create a str that has the pronounciation of the characters in a 
    string, e.g., "hello world" -> "You pronounce the letters in hello world like this: 
ash*euh*el*el*oh* *dooble-vay*oh*err*el*day*"
    '''
    str_to_pronounce = "hello world"
    
    # Open the file with letters and pronunciations
    with open(PRONOUNCE_FILE, "r") as infile:
        letters = infile.readline().split()
        letters.pop(0)
        pronounce_letters = infile.readline().split()
        pronounce_letters.pop(0)

    prononciation = ""
    for letter in str_to_pronounce: 
        # Look up the way to pronounce this letter
        cur_letter_pronunciation = " "
        for letter_idx in range(len(pronounce_letters)):
            
            if letters[letter_idx].lower() == letter.lower():
                cur_letter_pronunciation = pronounce_letters[letter_idx]
                break
        # OK, all done looking that up!
        
        prononciation += cur_letter_pronunciation + "*"
        
    
    print("You pronounce the letters in", str_to_pronounce, "like this: ")
    print(prononciation)
      
    
#pronounce_v1()


def get_letter_pronunciation(a_letter, letters, pronounces):
    '''
    Look up how to pronounce `a_letter` in the list of letter
    pronounciations, `pronounces`.
    '''
    cur_letter_pronunciation = " "
    for letter_idx in range(len(pronounces)):
        
        if letters[letter_idx].lower() == a_letter.lower():
            cur_letter_pronunciation = pronounces[letter_idx]
            break
        
    return cur_letter_pronunciation
            
    
def pronounce_str(str_to_pronounce):
    str_to_pronounce = "hello world"

    # Open the file with letters and pronunciations
    with open(PRONOUNCE_FILE, "r") as infile:
        letters = infile.readline().split()
        letters.pop(0)
        pronounce_letters = infile.readline().split()
        pronounce_letters.pop(0)

    pronunciation = ""
    for letter in str_to_pronounce: 
        cur_letter_pronunciation = get_letter_pronunciation(letter, 
                                                letters,
                                                pronounce_letters)
        
        pronunciation += cur_letter_pronunciation + "*"
        
    print("You pronounce the letters in", str_to_pronounce, "like this: ")
    print(pronunciation)
    
pronounce_str()

            