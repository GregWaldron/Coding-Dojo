def countdown (number):
    list = []
    for x in range (number, -1, -1):
        list.append(x)
    print (list)

def print_and_return (a,b):
    print(a)
    return b

def first_plus_length (list):
    print (list[0] + len(list))

def values_greater_than_second (list):
    newlist = []
    for x in range (0, len(list)):
        if list[x] > list[1]:
            newlist.append (list[x])
    print("Number of Values:", len(newlist))
    print("They are...", newlist)

def this_length_that_value(size, value):
    newlist=[]
    for x in range (0, size):
        newlist.append(value)
    print(newlist)
