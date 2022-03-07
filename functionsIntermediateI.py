
""" 
*  1. Update Values in Dictionaries and Lists   
"""
x = [[5, 2, 3], [10, 8, 9]]
students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'}
]
sports_directory = {
    'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer': ['Messi', 'Ronaldo', 'Rooney']
}
z = [{'x': 10, 'y': 20}]

""" 
? 1. Change the value 10 in x to 15.
     Once you're done, x should now be [ [5,2,3], [15,8,9] ].
"""
x[1][0] = 15
print("Updated x:", x)
print("")

"""
? 2. Change the last_name of the first student from 'Jordan' to 'Bryant'
"""
students[0]["last_name"] = "Bryant"
print("Updated students- first student:", students[0])
print("")

"""
? 3. In the sports_directory, change 'Messi' to 'Andres'
"""
sports_directory["soccer"][2] = "Andres"
print("Updated sports_directory-soccer:", sports_directory["soccer"])
print("")
"""
? 4. Change the value 20 in z to 30
"""

z[0]["y"] = 30
print("Updated z:", z)
print("")

""" 
*  2.Iterate Through a List of Dictionaries
    
    
? Create a function iterateDictionary(some_list) that, given a list of dictionaries,
    the function loops through each dictionary in the list and prints each key and
    the associated value.
    For example, given the following list:
"""

students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel


def iterateDictionary(arr):
    lineList = []
    for item in arr:
        for key in item:
            lineList.append(key)
            lineList.append(item[key])
        print(f"{lineList[0]} - {lineList[1]}, {lineList[2]} - {lineList[3]}")
        lineList = []
    return


iterateDictionary(students)
print("")


""" 
* Get Values From a List of Dictionaries

    Create a function iterateDictionary2(key_name, some_list) that,
    given a list of dictionaries and a key name,
    the function prints the value stored in that key for each dictionary.
    
    For example, iterateDictionary2('first_name', students) should output:

Michael
John
Mark
KB

And iterateDictionary2('last_name', students) should output:

Jordan
Rosales
Guillen
Tonel

"""


def iterateDictionary2(key_name, some_list):
    for item in some_list:
        print(item[key_name])
    return


iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)
print("")


""" 
* Iterate Through a Dictionary with List Values
    Create a function printInfo(some_dict) that given a dictionary whose values are all lists,
    prints the name of each key along with the size of its list,
    and then prints the associated values within each key's list.
    For example:

"""

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
# printInfo(dojo)
# output:
""" 
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


def printInfo(some_dict):
    for item in some_dict:
        print(f"{len(some_dict[item])} {item.upper()}")
        for x in some_dict[item]:
            print(x)
        print("")
    return


printInfo(dojo)
print("")
