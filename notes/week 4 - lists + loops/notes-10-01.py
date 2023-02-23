"""
byron wallace and ben rye
DS2k lecture 7 notes
"""

# TAKE THE QUIZ YOU RAT

a_list = ['a','b','c']
concat_str = ""

for letter in a_list:
    print(letter)
    concat_str += letter


SIMPSONS_FILE = "simpsons_data.tsv"


def simpsons():
    # solve to windows unicode problem -- otherwise encoding dsnt matter on mac
    simpsons_file = open(SIMPSONS_FILE, 'r', encoding="utf8")
    # topline of csv/tsv is like column titles

    bart_lines = []
    lisa_lines = []

    for line in simpsons_file:
        print(line)
        ...


simpsons()
