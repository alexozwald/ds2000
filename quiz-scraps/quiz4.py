#quiz4.py

# Q1
lst = [1, 2, 3]
for num in lst:
    print(num)


# Q2
lst = [1, 2, 3]
for i in range(len(lst)):
    print(i)


# Q3
total = 0
for i in range(len(lst)):
    total += lst[i]
print(total)


# Q4
max = 0
for num in lst:
    if num > max:
        num = max  # max = num
