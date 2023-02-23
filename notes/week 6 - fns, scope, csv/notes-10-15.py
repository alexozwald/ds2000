"""
Byron Wallace
DS2k lecture 11 notes

Scope
"""

import csv


SIMPSONS_CHARACTER_F = "simpsons_characters.csv"
SIMPSONS_SCRIPTS_F = "simpsons_script_lines.csv"


def read_simpsons_character_data():
    '''
    Read in the simpsons character data from the CSV

    returns list of characters:
        list [[character ID (int), name (str)], ...]
    '''
    with open(SIMPSONS_CHARACTER_F, 'r') as f:
        reader = csv.reader(f)
        header = next(reader)

        list_of_chars = []

        for row in reader:
            char_id, char_name = row[0:2]
            char_id = int(char_id)
            list_of_chars.append([char_id, char_name])

    return list_of_chars

def read_script_lines():
    '''
    Returns lines.
    '''
    CHAR_ID_INDX = 7
    RAW_TEXT_IDX = 3
    IS_SPEAKING_IDX = 5

    with open(SIMPSONS_CHARACTER_F,'r') as f:
        reader = csv.reader(f)
        header = next(reader)

        script_data = []

        for script_line in reader:
            # check if the script line is a piece of dialogue
            is_script_line = script_line[IS_SPEAKING_IDX] == "true"
            is_char_id = script_line[CHAR_ID_INDX] != ""

            if is_script_line and is_char_id:
                char_id = int(script_line[CHAR_ID_INDX])
                text = script_line[RAW_TEXT_IDX]
                script_data.append([char_id, text])

    return script_data


def list_of_character(name, list_of_chars):
    pass


def count_words_for_character(script_data, char_id):
    # return the number of words spoken by character character_id
    pass


def make_bar_plot(char_name, word_counts):
    pass


def main():
    # HE MAPPED OUT FUNC FOR WHAT TO DO BUT ITS LIKE NOT IMPORTANT IDK LOL
    # I KNOW HOW TO CODE SORRY SISTERRRRRRRRRRRR

    # get 

    #  

