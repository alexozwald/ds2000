"""
@author:    Alex Oswald
@class:     DS2000
@homework:  Homework 4
@date:      11 October 2021
"""

import matplotlib.pyplot as plt

FILE = "hotspur.txt"

'''SAMPLE OUTPUT:
...
'''

def tottenham():
    # read file with while loop
    with open(FILE, 'r') as f:
        line = None
        goals = []  # goals record
        wld = []    # win / loss / draw
        while True:
            line = f.readline().rstrip()
            # break loop if no new line to read
            if (line == ""):
                break
            goals.append(line.split(' '))
            line = f.readline().rstrip()
            wld.append(line.split(' '))

    #############
    # Problem 1 #
    #############

    # reduce complexity + readability with nested func
    problem1(goals, wld)

    #############
    # Problem 2 #
    #############

    # init lists to count each szn
    wins_ct = [0] * len(goals)
    goal_ct = [0] * len(goals)
    for i in range(len(goals)):
        for j in range(len(goals[i])):
            # ignore szn id
            if (j == 0):
                continue

            # tally goals from every match
            goal_ct[i] += int(goals[i][j])

            # tally if game was won
            if (wld[i][j] == 'W'):
                wins_ct[i] += 1

    # calc least/most wins or goals -- by index so szn id can be grabbed
    least_wins_idx = wins_ct.index(min(wins_ct))
    most_goals_idx = goal_ct.index(max(goal_ct))

    print("\n\nSeason with the fewest wins:  " + goals[least_wins_idx][0])
    print("Season with the most goals:   " + goals[most_goals_idx][0])

    #############
    # Problem 3 #
    #############
    # _option 2_

    # gather data for WLD/goals
    scatter_title = "Tottenham Club " + goals[0][0] + " Season"
    wins_x = []
    wins_y = []
    loss_x = []
    loss_y = []
    draw_x = []
    draw_y = []
    for j in range(len(goals[0])):
        if wld[0][j] == 'W':
            wins_x.append(j)
            wins_y.append(int(goals[0][j]))
        elif wld[0][j] == 'L':
            loss_x.append(j)
            loss_y.append(int(goals[0][j]))
        elif wld[0][j] == 'D':
            draw_x.append(j)
            draw_y.append(int(goals[0][j]))
        else:
            continue

    # plot scatter
    plt.scatter(wins_x, wins_y, color='#06d6a0', label='Win')
    plt.scatter(loss_x, loss_y, color='#ef476f', label='Loss')
    plt.scatter(draw_x, draw_y, color='#ffd166', label='Draw')
    plt.xlabel("Game of Season")
    plt.ylabel("Goals Scored")
    plt.legend()
    plt.title(scatter_title)

    # display plot
    plt.show()


def problem1(goals, wld):
    for i in range(len(goals)):
        # current season + amt of games played
        season = goals[i][0]
        match_ct = len(goals[i]) - 1    # -1 for szn ID
        szn_id = [season, match_ct]
        
        # Tottenham win/lose/draw count
        wins = 0
        loss = 0
        draw = 0
        for game in wld[i]:
            if game == 'W':
                wins += 1
            elif game == 'L':
                loss += 1
            elif game == 'D':
                draw += 1
            else:
                continue
        match_results = [wins, loss, draw]

        # win with 1 goal
        win_with_one = 0
        for game in range(len(wld[i])):
            if (wld[i][game] == 'W') and (goals[i][game] == '1'):
                win_with_one += 1

        # szn_results
        szn_results = 0
        for game in wld[i]:
            if game == 'W':
                szn_results += 3
            elif game == 'L':
                szn_results += 0
            elif game == 'D':
                szn_results += 1
            else:
                continue

        # print results
        print_szn(szn_id, match_results, win_with_one, szn_results)


def print_szn(season, match_results, win_with_one, szn_results):
    # convert to strings
    season[1] = str(season[1])
    match_results = [str(x) for x in match_results]
    win_with_one = str(win_with_one)
    szn_results = str(szn_results)

    # print results pretty ~
    print("Season:  " + season[0] + ' (' + season[1] + ' games)')
    print("--")
    print("Match results...")
    print("\tWins:      " + match_results[0])
    print("\tLosses:    " + match_results[1])
    print("\tDraws:     " + match_results[2])
    print("Won with 1 goal:   " + win_with_one)
    print("Tottenham score:   " + szn_results)
    print()


tottenham()
