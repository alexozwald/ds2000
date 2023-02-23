"""
@author:    Alex Oswald
@class:     DS2000
@homework:  Homework 7
@date:      15 November 2021

Attributes:
    CSV_FILE (str): Description
"""

import csv
import json
#import pprint
import matplotlib.pyplot as plt
import matplotlib.cm


#NAMES = ["JAKE". "ROSA". "GINA". "HOLT". "AMY". "TERRY"]
CSV_FILE = "b99_lines.csv"


def prob1(filename, names_list):
    """Read in csv of each characters lines to make a wordlist-wordcount
    dictionary for each supplied name + encompass them all in a dictionary
    
    Args:
        filename (str): string to read in, likely constant var
        names_list (list[strs]): list of names -> whose lines will be read
    
    Returns:
        dict[dicts]: name-dictionary of dictionaries
    """
    # create data_dict
    data_dict = {}
    for name in names_list:
        data_dict[name] = {}  # init dict per person

    # open file
    with open(filename, 'r') as f:
        reader = csv.reader(f, delimiter=',')

        for row in reader:
            if row[0] in names_list:
                #curr_name = row[0]
                for item in row[1:]:
                    item = item.lower()
                    if (item in data_dict[row[0]]) and (item != ''):
                        data_dict[row[0]][item] += 1
                    elif (item != ''):
                        data_dict[row[0]][item] = 1
            #data_dict.append(json.loads(row))

    return data_dict


def prob2_sort(data_dict):
    """Sort supplied dictionary within dictionary descending by values for each
    object in the dictionary.
    
    Args:
        data_dict (dict): dictionary of name-dicts containing words + word cts
    
    Returns:
        dict: sub-sorted version of data_dict
    """
    # sort dictionary of dictionaries
    sorted_dict = {}
    for name in data_dict:
        # sort per-name dict
        name_dict = dict(sorted(data_dict[name].items(), key=lambda item: item[1], reverse=True))
        # appent per-name sorted dict to new dict
        sorted_dict[name] = name_dict

    return sorted_dict


def prob2_top_n(sorted_dict, top_n):    
    """Extract a truncated dictionary with only the top-N (supplied) words
    
    Args:
        sorted_dict (dict[dicts]): pre-sorted dict of dicts {name{word:counts}}
        top_n (int): amount of top-words to extract
    
    Returns:
        TYPE: sorted_dict with each sub-dict only containing the TOP_N words
    """
    # separate dict by n
    top_n_dict = {}
    for name in sorted_dict:
        top_n_dict[name] = dict(list(sorted_dict[name].items())[0:top_n])
        #top_n_dict[name] = sorted_dict[name].items()[0:top_n]

    # print dict
    # __make comma separated string of select names in title case__
    names_str = ', '.join(list([x.title() for x in list(sorted_dict.keys())]))
    print("Dictionary view of the Top", top_n, "words spoken by", names_str + ':')
    print(json.dumps(top_n_dict, indent=4))
    #pprint.pp(top_n_dict, indent=3`)

    return top_n_dict


def prob3(sorted_dict):
    """Prompt the user to enter one of your three characters. Draw a plot of 
    that character’s top-n words.
    
    Args:
        sorted_dict (dict): pre-sorted dict of dicts {names{words:counts}}
    """
    # Prompt the user to enter one of your three characters
    # print options + get input for which character
    names_str = ', '.join(list([x.title() for x in list(sorted_dict.keys())]))
    question0 = "Which character would you like to evaluate (e.g. " + names_str + ")?  "
    name = input(question0).lower()  #name='jake'

    question1 = "How many top-words do you want to evaluate?  "
    top_n = int(input(question1))    #top_n=9

    # get lists for top words + counts...
    y_wordct = list(sorted_dict[name.upper()].values())[0:top_n]
    y_labels = list(sorted_dict[name.upper()].keys())[0:top_n]

    # set colormaps
    cmap = matplotlib.cm.get_cmap('Pastel2')
    cmap2 = matplotlib.cm.get_cmap('Set2')

    # Draw a plot of that character’s top-n words
    x_base = range(0, top_n)

    plt.bar(y_labels, y_wordct, color=cmap.colors, edgecolor=cmap2.colors)
    # gen title
    title_str = "Analysis of " + name.title() + "'s Speech in Brooklyn 99"
    plt.title(title_str)
    # gen axes titles
    x_label = f"Top {top_n} Words"
    plt.xlabel(x_label)
    plt.ylabel("Wordcounts")

    plt.show()



if __name__ == '__main__':
    # problem 1
    my_names = ["JAKE", "TERRY", "GINA"]
    my_names_word_cts = prob1(CSV_FILE, my_names)

    # problem 2
    sorted_dict = prob2_sort(my_names_word_cts)
    top_n_dict = prob2_top_n(sorted_dict, 3)

    # problem 3
    prob3(sorted_dict)
