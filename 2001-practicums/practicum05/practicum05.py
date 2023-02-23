#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@class:       DS 2001 (Fall 2021)
@prof:        Ryan Gallagher
@author:      Alex Oswald
@date:        2021-10-11
@descr:       Practicum 05
"""

import matplotlib.pyplot as plt

SHOOTING_FILE = "fatal-police-shootings-data_cleaned.tsv"
POP_FILE = "state_population.csv"


def main():
    # define variablkes
    shooting = []  # thiccy data file - 2D matrix
    date = []
    age = []

    with open(SHOOTING_FILE, 'r') as f:
        for line_num,line in enumerate(f):
            if line_num == 0:
                continue
            line = line.rstrip().split('\t')
            
            shooting.append(line)  # 2D list
            date.append(line[2])
            age.append(int(line[5]))

    '''shootings[:][x] map
    line[0]     shoot_id
    line[1]     name
    line[2]     date
    line[3]     manner_of_death
    line[4]     armed
    line[5]     age
    line[6]     gender
    line[7]     shoot_race
    line[8]     shoot_city
    line[9]     shoot_state
    line[10]    signs_of_mental_illness
    line[11]    threat_level
    line[12]    flee
    line[13]    body_camera
    line[14]    longitude
    line[15]    latitude
    line[16]    is_geocoding_exact
    '''


    #################################
    # 1 DESCRIBING POLICE SHOOTINGS #
    #################################

    '''requested comment:  print all names
    print(', '.join(name))
    '''

    total_killed = len(shooting)

    # find percentage killed that are black men
    black_men = 0
    for i in shooting:
        if (i[7] == 'B') and (i[6] == 'M'):
            black_men += 1

    percent_blackmen = black_men / total_killed * 100

    youngest = min(age)
    oldest = max(age)
    avg_age = sum(age) / total_killed

    # print
    percent_blackmen_str = str(round(percent_blackmen,1))
    avg_age_str = str(round(avg_age,1))
    youngest_str = str(youngest)
    oldest_str = str(oldest)
    
    print("Total # of shootings:     " + str(total_killed))
    print("% killed are black men:   " + percent_blackmen_str + '%')
    print()
    print("Youngest police shooting victim:     " + youngest_str, "years old")
    print("Oldest police shooting victim:       " + oldest_str, "years old")
    print("Average police shooting victim age:  " + avg_age_str, "years old")

    ################################
    # 2 POLICE SHOOTINGS OVER TIME #
    ################################

    # get years list
    date_yr = []
    for i in date:
        year = int(i[0:4])
        if year not in date_yr:
            date_yr.append(year)

    # calc shootings per year
    shootings_per_year = [0] * len(date_yr)
    for i in range(0,len(date_yr)):
        for j in date:
            if int(j[0:4]) == date_yr[i]:
                shootings_per_year[i] += 1
            elif int(j[0:4]) > date_yr[i]:
                break

    # plot data
    plt.plot(date_yr, shootings_per_year, '-o', color='black')
    plt.xlabel("Year")
    plt.ylabel("# of Fatal Police Shootings")
    plt.ylim(ymin=0)
    # plot will open at end


    # 3 POLICE SHOOTING INEQUITIES

    # read file
    state_pop = []  # 2D data list
    with open(POP_FILE, 'r') as f:
        for line_num,line in enumerate(f):
            if line_num == 0:
                continue

            line_strs = line.rstrip().split(',')
            line_ = line_strs[0]
            line__ = [float(x) for x in line_strs[1:]]
            line__.insert(0,line_)
            state_pop.append(line__)

    # process data per state for ...
    # returns:  total shootings,  (for all races)
    # stats-> [state_id, kills, race[id,ct,pop%,FF%], race[id,ct,pop%,FF%],
    #          race[id,ct,pop%,FF%], race[id,ct,pop%,FF%], race[id,ct,pop%,FF%]]
    state_stats = []            # 50 states

    # for each state --> for each race --> loop shooting[] to add nums
    temp_state = [None] * 7     # 7 items / sublist (see above)
    temp_race = [None] * 4      # 4 items / sub-sublist = [id, count, pop%, FF%]
    for i in range(0,len(state_pop)):
        temp_state = [None] * 7
        temp_race = [None] * 4

        # set state
        state = state_pop[i][0]
        
        # sum state total
        state_total = 0
        for w in range(0,total_killed):
            if shooting[w][9] == state:
                state_total += 1

        # loop for each race
        for j in range(1,len(state_pop[i])):
            # find race from index
            race = find_race(j)[0]

            # pop %
            pop_prcnt = state_pop[i][j]

            # fatal force %
            race_total = 0

            for k in range(0,total_killed):
                if shooting[k][9] == state and shooting[k][7] == race:
                    race_total += 1

            ff_prcnt = race_total / state_total * 100

            # fill sub-lists for insertion
            temp_race = [race, race_total, pop_prcnt, ff_prcnt]
            temp_state[ j + 1 ] = temp_race

        # add back to state_stats dataset
        temp_state[0] = state
        temp_state[1] = state_total
        state_stats.append(temp_state)

    print_state_data(state_stats)

    plt.show()
    ## end of main()


def print_state_data(stats):
    '''state_stats structure:
    [ ID, #kills, race_list1, race_list2, race_list3, race_list4, race_list5 ]
    race_listX = [ race, race_total, pop_prcnt, ff_prcnt ]
    '''
    for i in range(0, len(stats)):
        print(stats[i][0])      # print state
        print("--")
        print(str(stats[i][1]), "shootings in total")
        print("NOTE:  total %s will not add up to 100")
        print()
        for j in range(2, 7):
            race_str = find_race(stats[i][j][0])[1]
            race_ttl = str(stats[i][j][1])
            race_pps = str(round(stats[i][j][2],2))
            race_ffs = str(round(stats[i][j][3],2))
            print(race_str, '(' + race_ttl + ')')
            print('\t' + race_pps + '%', "(population share)")
            print('\t' + race_ffs + '%', "(Fatal Force share)")
            print()


def find_race(var):
    # var is one of 2 values:
    #    -  index in state_pop[...][var]
    #    -  char returned earlier fn call
    # match (var): case: ... added in python 3.10 --> not yet implemented
    if (var == 1) or (var == 'W'):
        race = 'W'
        name = "White"
    elif (var == 2) or (var == 'B'):
        race = 'B'
        name = "Black"
    elif (var == 3) or (var == 'N'):
        race = 'N'
        name = "Native American"
    elif (var == 4) or (var == 'A'):
        race = 'A'
        name = "Asian"
    elif (var == 5) or (var == 'H'):
        race = 'H'
        name = "Hispanic"
    else:
        print("ERROR")
        return None

    return race, name


main()
