'''
counter = 1

while counter <= 15:
    print(counter)
    counter += 1

print()
'''

# a slightly different way
counter = 1
while True:
    #print(counter)
    counter += 1
    if counter > 15:
        break


new_list = [1,3,5]
other_list = [5,10,12]
final_list = new_list + other_list
print(new_list)
print(other_list)
print(final_list,'\n')


simple_list = [56]

simple_list.insert(0, 'hello')  # not natural in python
print(simple_list)

simple_list.pop(0)
print(simple_list)

simple_list.append(43)
print(simple_list,'\n')


def func():
    a_list = ['x', 5, 10, -3, "hello", "stop", "1000", "whaatever", 6]
    new_list2 = []

    cur_index = 0
    element = a_list[cur_index]

    while not element == "stop":
        print(element)
        cur_index += 1
        element = a_list[cur_index]

    while element != "stop":
        new_list2.append(element)
        #cur_index += 1
        print("cur_index is:", cur_index)
        print("a_list is:", a_list)
        element = a_list.pop(cur_index)

    new_list3 = []
    while len(a_list) > 0:
        element = a_list.pop(0)
        new_list3.append(element)


func()

