import json

file = open('familyTree.json')
treeData = json.load(file)
file.close()


def iterate(obj):
    print(obj['Name'])
    print(obj['BirthYear'])
    print(obj['DeathYear'])
    age=int(obj['DeathYear'])-int(obj['BirthYear'])
    print('Age of ', obj['Name'], ": ", age)
    if(age < 12 or age > 120):
        print(obj['Name'], "is an error Node")
    print()

    if(obj.get('Members')):
        for i in range(len(obj['Members'])):
            iterate(obj['Members'][i])
       

dict = treeData['lineage']['Members']
for i in range (len(dict)):
    iterate(dict[i])

