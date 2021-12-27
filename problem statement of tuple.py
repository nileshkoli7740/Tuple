##Write a Python program to create a tuple with numbers and print one item.
"""tuplex = 5,10,20,30,45
print(tuplex)
tuplex =10,
print(tuplex)

#Write a Python program to add an item in a tuple.
tuplex = (4,3,5,7,8,1,2)
print(tuplex)
tuplex = tuplex + (9,)
print(tuplex)
tuplex = tuplex[:5] + (15,20,25) + tuplex[:5]
print(tuplex)
listx = list(tuplex)
listx.append(30)
tuplex = tuple(listx)
print(tuplex)

tuplex  = (1,2,3,4,5,6,7)
print(tuplex)
tuplex = tuplex + (8,)
print(tuplex)
tuplex = tuplex[:6] + (20,30,40) + tuplex[:6]
print(tuplex)
listx = list(tuplex)
listx.append(50)
tuplex = tuple(listx)
print(tuplex)

#Write a Python program to convert a tuple to a string.
tuple = ('e','x','e','r','s','i','e','s')
str = ''.join(tuple)
print(len(tuple))
print(len(str))
print(str)

t = ('n','i','l','e','s','h','k','o','l','i')
str = ''.join(t)
print(len(str))
print(str)

#Write a Python program to get the 4th element and 4th element from last of a tuple.
t = ('w','3','r','e','s','o','u','r','s','e')
print(t)
#to get of 4th element
item = t[4]
print(item)
item1 = t[-4]
print(item1)

#Write a Python program to find the repeated items of a tuple.
tuplex = 2, 4, 5, 6, 2, 3, 4, 4, 7, 4, 5, 7, 4
print(tuplex)
count = tuplex.count((4))
print(count)

a = 1,2,2,1,2,2,3,3,4,5,4,2,2
print(a)
count = a.count(2)
print(count)

#Write a Python program to check whether an element exists within a tuple.
tuplex = ("w", 3, "r", "e", "s", "o", "u", "r", "c", "e")
print("r" in tuplex )
print(5 in tuplex)

t = (1,2,3,4,5,6,7,8,9)
print(t)
t = t[:5] + (10,15,20) + t[:5]
print(t)
l = list(t)
l.append(40)
t = tuple(l)
print(t)

#Write a Python program to convert a list to a tuple.
listx = [10,20,30,40,50,60]
print(listx)
tuplex = tuple(listx)
print(tuplex)

#Write a Python program to remove an item from a tuple.
tuplex = "w", 3, "r", "s", "o", "u", "r", "c", "e"
print(tuplex)
tuplex = tuplex[:2] + tuplex[3:]
print(tuplex)
listx = list(tuplex)
listx.remove("c")
tuplex = tuple(listx)
print(tuplex)

tuplex = "w", 3, "r", "s", "o", "u", "r", "c", "e"
print(tuplex)
tuplex = tuplex [:3] + tuplex [4:]
print(tuplex)
listx = list(tuplex)
listx.remove("c")
tuplex = tuple(listx)
print(tuplex)

#Write a Python program to find the index of an item of a tuple.
tuplex = tuple("index tuple")
print(tuplex)
index = tuplex.index("p",5)
print(index)
index1 = tuplex.index("e",3,9)
print(index1)
index2 = tuplex.index("l",9)
print(index2)

a = tuple("nilesh koli")
print(a)
index = a.index("k")
print(index)
index1 = a.index("i")
print(index1)
index2 = a.index("s")
print(index2)

#Write a Python program to find the length of a tuple.
tuplex = tuple("w3resource")
print(tuplex)
print(len(tuplex))

a = tuple("nilesh koli")
print(a)
print(len(a))

#Write a Python program to convert a tuple to a dictionary.
tuplex = ((2, "w"),(3, "r"))
print(dict((y,x) for x,y in tuplex))

a = ((1,"a"),(2,"b"))
print(a)
print(dict((y,x) for x, y in a))

#Write a Python program to reverse a tuple.
x = ("w3resource")
y = reversed(x)
print(tuple(y))
x1 = (5,10,15,20)
y1 = reversed(x1)
print(tuple(y1))

#Write a Python program to unzip a list of tuples into individual lists.
l = [(1,2),(3,4),(8,9)]
print(list(zip(*l)))

x = ("nileshkoli")
y = reversed(x)
print(tuple(y))

x = ((2,"a"),(3,"b"))
print(dict((n,m) for m,n in x))

a = [(1,2),(3,4),(8,9)]
print(list(zip(*a)))

#Write a Python program to convert a list of tuples into a dictionary.
l = [("x",1),("x",2),("x",3),("y",4),("y",5),("z",6)]
d = {}
for a,b in l:
    d.setdefault(a,[]).append(b)
print(d)

a = [('a',1),('a',2),('a',3),('b',4),('b',5),('c',6)]
d = {}
for x,y in a:
    d.setdefault(x,[]).append(y)
print(d)
Write a Python program to replace last value of tuples in a list.
l = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
print([t[:-1] + (100,) for t in l])
"""
#Write a Python program to replace last value of tuples in a list.
a = [(10,20,30),(40,50,60),(70,80,90),(100,110,120)]
print([t[:-1] + (100,) for t in a])