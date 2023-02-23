#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DS2k Lecture 12 Notes: 
    Revisiting the Simpsons, with dictionaries!

Byron Wallace and Ben Nye
"""

"""
The goal: Using data in two CSV files (one listing Simpsons character 
information, and one comprising lines from the show), we want to write a 
program that will accept a list of character names, and visualize the 
amount of dialogue they engage in (i.e., number of lines).
"""

import csv 
import matplotlib.pyplot as plt 

SIMPSONS_CHARACTERS_FILE = "simpsons_characters.csv"
SIMPSONS_SCRIPTS_FILE    = "simpsons_script_lines.csv"

def read_in_characters():
    """
    Read in the Simpsons character data from the CSV>

    Returns
    -------
    A dict mapping character names to IDs for all characters in the Simpsons.
    """
        
    # Note that notation here; {} rather than [], meaning dictionary, not list.
    characters_d = {}
        
    with open(SIMPSONS_CHARACTERS_FILE, "r") as simpsons_characters:
        reader = csv.reader(simpsons_characters)
        # Pull off the headers, which we don't really need
        headers = next(reader)
        
        for character_row in reader:
            # We only want the ID (element 0) and name fields (1)
            char_id, char_name = character_row[:2]
            # Note that we lowercase all names
            characters_d[char_name.lower()] = int(char_id)
            
    return characters_d


def read_in_script_lines():
    """
    Reads in the `script lines' data from the corresponding CSV

    Returns
    -------
    A dictionary mapping from character IDs (int) to lines (str)

    """
    # Q: Why make these "local" variables?
    TEXT_IDX, CHAR_ID_IDX = 3, 6
    IS_SPEAKING_LINE_IDX = 5
    
    script_d = {}
    
    with open(SIMPSONS_SCRIPTS_FILE , "r") as simpsons_script_lines:
        reader = csv.reader(simpsons_script_lines)
        
        # Again advance past the headers
        headers = next(reader)
        
        for script_line in reader:
            # Note! If we attempt to do this for *all* lines, we
            # get into trouble because there are no character IDs
            # for "non-speaking" lines! So we have to check if the
            # current line is a speaking line — we only care about 
            # these. There are also a few cases where there is no
            # character ID given, in which case we will also skip
            # the line. 
            is_script_line = script_line[IS_SPEAKING_LINE_IDX] == "true"
            has_character_id = script_line[CHAR_ID_IDX] != ""
            if is_script_line and has_character_id:
                character_id = int(script_line[CHAR_ID_IDX])
                # We get rid of the 'Name:' part of the script.
                # *Technically* this might intro a bug where
                # a colon is used in the text itself but let's
                # ignore this.
                text = script_line[TEXT_IDX].split(":")[1]
                
                # This is a bit tricky because there are two
                # cases: (1) the dictionary already contains the
                # character ID, in which case we want to append
                # to the list; (2) we need to add the character
                # to the dictionary, with just this line in a list
                # at first.
                if character_id in script_d:
                    script_d[character_id].append(text)
                else:
                    script_d[character_id] = [text]

    return script_d

# We can basically just drop this function, since dictionaries
# naturally provide this "look-up" functionality!
'''
def get_id_for_name(characters_list, char_name):
    """
    Return the name associated with the given character ID.

    Parameters
    ----------
    characters_d : dict with int keys and str values
        List of tuples comprising character identifiers and names
    char_name : str
        String identifier for character e.g. "Bart Simpson"

    Returns
    -------
    The name associated with the given ID. If we cannot find this, then
    None.

    """
    for char_id_and_name in characters_list:
        if char_id_and_name[1].lower() == char_name.lower():
            return char_id_and_name[0]
    # Q: What if we never find the character? 
'''

def count_words_in_line(line):
    """ Counts and returns the number of words in line (str). """
    return len(line.split())

def get_num_words_for_char(character_id, script_d):
    """
    Return the total number of words spoken by the character
    associated with the given ID.
    
    Parameters
    ----------
    character_id : integer
        Integer identifier for character
      
    script_data : dict
        Maps character IDs (int) to their lines (str)
        
    Returns
    -------
    An integer count of the number of words spoken by said person.
    """
    
    # Again we can replace the look up logic with the 
    # dictionary
    total_count_for_char = 0
    for line in script_d[character_id]:
        total_count_for_char += count_words_in_line(line)
    
    '''
    for line_data in script_data:
        cur_char_id, line = line_data[1], line_data[2]
        if cur_char_id == character_id:
            total_count_for_char += count_words_in_line(line)
    '''
    
    return total_count_for_char


def viz_line_counts(character_names):
    """
    Using the data in the CSV files, we will plot the number of lines
    for each character, assuming we can find them. 

    Parameters
    ----------
    characters : TYPE
        List of strings specifying characters of interest (full names)

    Returns
    -------
    None.
    """
    
    # Read in the data: Now both of these will be 
    # *dictionaries*, instead of lists of lists.
    characters_dict = read_in_characters()
    script_dict     = read_in_script_lines()
    
    # Look up the IDs for the given characters
    #character_ids = [get_id_for_name(characters_list, name)
    #                  for name in character_names]
    # Check if we failed to find any; if so, exit.
    # if None in character_ids:
    #    print("Sorry, I couldn't find all of those characters!")
    #    return 
    
    # character_ids = [characters_dict[name.lower()] for name in character_names]
    character_ids = []
    # Lower case to normalize
    for name in character_names:
        if name.lower() in characters_dict:
            character_ids.append(characters_dict[name.lower()])
        else:
            print("Sorry, I couldn't find", name)
            return None
    
    # Otherwise, look up line counts for each character
    word_counts = [get_num_words_for_char(id_, script_dict) 
                    for id_ in character_ids]

    plt.bar(character_names, word_counts)
    
        
# viz_line_counts(["bart simpson", "gil gunderson", "comic book guy"])

def main():
    done = False
    characters = []
    while not done:
        character = input("Enter a Simpsons character (full name) or 'done':")
        if character == "done":
            done = True
        else:
            characters.append(character)

    viz_line_counts(characters)
    
if __name__ == "__main__":
    main()

        