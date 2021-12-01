def countdown (number):
    list = []
    for x in range (number, -1, -1):
        list.append(x)
    print (list)
countdown(15)

def print_and_return (list):
    print(list[0])
    return list[1]
print_and_return ([30,13])

def first_plus_length (list):
    return (list[0] + len(list))
print(first_plus_length ([27,30,13,31,17,33]))

def values_greater_than_second (list):
    newlist = []
    if len(list)<2:
        return False
    for x in range (0, len(list)):
        if list[x] > list[1]:
            newlist.append (list[x])
    print("Number of Values:", len(newlist))
    return newlist
values_greater_than_second ([27,30,13,31,17,33])

def this_length_that_value(size, value):
    newlist=[]
    for x in range (0, size):
        newlist.append(value)
    print(newlist)
this_length_that_value(10,13)