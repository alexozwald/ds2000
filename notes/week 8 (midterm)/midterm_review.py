"""
MIDTERM REVIEW
"""

print(range(4,11,3))

for i in range(10):
  	if (i + 1) > 2 and (i % 2 == 0):
         print("i is " + str(i))
      

def count_blank_lines(filename):
  """
  Return the number of blank lines in the given file
  """
  with open (filename,"r") as infile:
      lines = infile.readlines()
      
  num_blank_lines = 0
  for i in range(0, len(lines)):
      if lines[i].strip() == "":
          num_blank_lines += 1
  
  return num_blank_lines


def calc_means(list_of_rows):
  """
  [[1,7,7], [4,3,3] ... [8.5,3.9]
  """
  column_means = [0,0]
  
  n_rows = len(list_of_rows)
  
  for cur_row in list_of_rows:
      column_means[0] += curr_row[0]
      column_means[1] += curr_row[1]
  
  column_means[0] = column_means[0] / n_rows
  column_means[1] = column_means[1] / n_rows
  
  return column_means



## STOCKS

'''
data...
'''

import csv
import matplotlib.pyplot as plt

def pct_change(new_value, old_value):
  return (new_value - old_value) / old_value * 100

def calc_pct_changes(csv_data):
  stock_names = csv_data[0][1:]
  # assuming ordered by date
  first_day_row = csv_data[1]
  #last_day_row = csv_data[len(csv_data)-1]
  # OR
  last_day_row = csv_data[-1]
  
  # variables to keep track of
  max_change, max_stock_idx = None, None
  
  for stock_idx in range(1, len(stock_names)+1):
      end_of_year_val = float(last_day_row[stock_idx])
      start_of_year_val = float(first_day_row[stock_idx])
      cur_change = pct_change(end_of_year_val, start_of_year_val)
      print("Stock: ", stock_names[stock_idx-1], "Change: ", cur_change)
      
      if max_change is None or cur_change > max_change:
          max_change = cur_change
          max_change_idx = stock_idx
          
  return max_stock_idx
  
  
  
  

def main():
  with open("stocks.csv", 'r') as csv_file:
      # list of lists
      csv_data = list(csv.reader(csv_file, delimeter=","))
  
  
  























