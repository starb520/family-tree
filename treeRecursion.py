import json

# open file, read file into a variable, close file
file = open('familyTree.json')
treeData = json.load(file)
file.close()

#### Function for iterating through a dictionary object
def iterate(obj):
    print(obj['Name'])
    print(obj['BirthYear'])
    print(obj['DeathYear'])

    # calculate age to display
    age=int(obj['DeathYear'])-int(obj['BirthYear'])
    print('Age of ', obj['Name'], ": ", age)

    # if the age of a member of a family is negative
    # or too large, display an error message
    if(age < 12 or age > 120):
        print(obj['Name'], "is an error Node")
    print()
    print('****************')

    # continue to iterate through family members until
    # there are no longer family members listed
    if(obj.get('Members')):
        
        for i in range(len(obj['Members'])):
            iterate(obj['Members'][i])


# get to the level of the dictionary needed to access 'Members'
dict = treeData['lineage']['Members']

# iterate through each part of the first generation
for i in range (len(dict)):
    iterate(dict[i])

