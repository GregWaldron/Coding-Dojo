#Update Values in Dictionaries and Lists

x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

x[1][0] = 15
# print(x)
students[0]["last_name"]="Bryant"
# print(students[0])
sports_directory["soccer"][0]="Andres"
# print (sports_directory["soccer"][0])
z[0]["y"]="z"
# print (z)



#Iterate Through a List of Dictionaries

def iterateDictionary(some_list):
    for x in range (0, len(some_list)):
        print ("first_name - " + some_list[x]["first_name"] + ", last_name - " + some_list[x]["last_name"])

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
# iterateDictionary(students) 
"""
should output: (it's okay if each key-value pair ends up on 2 separate lines;
bonus to get them to appear exactly as below!)
first_name - Michael, last_name - Jordan
first_name - John, last_name - Rosales
first_name - Mark, last_name - Guillen
first_name - KB, last_name - Tonel
"""


#Get Values From a List of Dictionaries

def iterateDictionary2(key_name, some_list):
    for x in range (0, len(some_list)):
        print (some_list[x][key_name])

# iterateDictionary2 ("last_name", students)



#Iterate Through a Dictionary with List Values

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
    key_list=[]
    for x in some_dict:
        key_list.append(x)
        print (str(len(some_dict[x])) + " " + str(x.upper()))
        for y in range (0, len(some_dict[x])):
            print(some_dict[x][y])
        print (" ")

# printInfo(dojo)

"""
# output:
7 LOCATIONS
San Jose
Seattle
Dallas
Chicago
Tulsa
DC
Burbank
    
8 INSTRUCTORS
Michael
Amy
Eduardo
Josh
Graham
Patrick
Minh
Devon
"""
