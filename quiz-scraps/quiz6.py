#quiz6.py

# Q2
lst = [["a", "b", "c"], ["d", "e", "f", "g"]]
print("a" in lst)
print(len(lst) == 7)
print(["a", "b", "c"] in lst)
print(["d", "e", "f"] in lst)

# Q3
dctn = {}
dctn[1980] = "a"
dctn[1990] = "b"
dctn[2000] = "c"
dctn[1990] = "d"
print(dctn)

# Q4
class ClassName(object):
    """docstring for ClassName"""
    def __init__(self, arg):
        super(ClassName, self).__init__()
        self.arg = arg

#Q5
class Foo:
    """docstring for Foo"""
    def __init__(self, x=""):
        super(Foo, self).__init__()
        self.x = x


a = Foo()
print(a.x)
a.x = "my foo"
print(a.x)

b = Foo()
b.x = "my foo"
print(a.x == b.x)
print(a is b)

