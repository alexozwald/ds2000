#quiz5.py

# Q3
def do_math(a, b):
    result = a / b
    return result
    result = result + 5


x = do_math(20, 5)
print(x)


#Q4
def eggs(a):
    a += 4
    return a


def spam(a):
    a = a * 2
    return eggs(a)


def main():
    a = 18
    result = spam(a)
    print(result)


main()

#Q5
def eggs2(c):
    c += 4
    return c

def spam2(b):
    b = b * 2
    return eggs2(b)

def main2():
    a = 18
    result = spam2(a)
    print(result)

main2()

