import json
import pandas as pd



file = open('familyTree.json')
treeData = json.load(file)
file.close()
df = pd.DataFrame(treeData['lineage']['Members'])

#### Generation One First half
print()
print()
# Gen1A
gen1 = treeData['lineage']['Members'][0]
gen1 = pd.json_normalize(gen1, max_level=20)
gen1['Ages'] = (gen1['DeathYear'].astype(int)-gen1['BirthYear'].astype(int))
print("First Generation")
print(gen1.sort_values(by = 'Ages'))                 ## display by ages
print('\t The median age: ', gen1['Ages'].median())  ## find median age for this generation
print('\t The mean age: ', gen1['Ages'].mean())      ## find mean age for this generation
print('\t Generation Count: ', gen1['Name'].count()) 
# print(gen1)                                        ## display by order in dictionary
print()

# Gen1A->Gen2A
gen2 = treeData['lineage']['Members'][0]['Members']
gen2 = pd.json_normalize(gen2, max_level=20)
gen2['Ages'] = (gen2['DeathYear'].astype(int)-gen2['BirthYear'].astype(int))
print("Second Generation")
print(gen2.sort_values(by = 'Ages'))                 ## display by ages                                 
print("\t The median age:", gen2['Ages'].median())
print("\t The mean age:", gen2['Ages'].mean()) 
print('\t Generation Count: ', gen2['Name'].count()) 
# print(gen2)                                        ## display by order in dict                               
print()

# Gen1A->Gen2A->Gen3A
gen3A = treeData['lineage']['Members'][0]['Members'][0]['Members']
gen3A = pd.json_normalize(gen3A, max_level=20)
gen3A['Ages'] = (gen3A['DeathYear'].astype(int)-gen3A['BirthYear'].astype(int))
print("Third Generation")
print(gen3A.sort_values(by = 'Ages'))              ## puts the values in ascending order by ages
print("\t The median age:", gen3A['Ages'].median())
print("\t The mean age:", gen3A['Ages'].mean()) 
print('\t Generation Count: ', gen3A['Name'].count()) 
# print(gen3A)                                     ## display by order in dict   
print()


## Gen1A->Gen2A->Gen3B
gen3B = treeData['lineage']['Members'][0]['Members'][1]['Members']
gen3B = pd.json_normalize(gen3B, max_level=20)
gen3B['Ages'] = (gen3B['DeathYear'].astype(int)-gen3B['BirthYear'].astype(int))
print("Third Generation")
print(gen3B.sort_values(by = 'Ages')) 
# print(gen3B)
print("\t The median age:", gen3B['Ages'].median())
print("\t The mean age:", gen3B['Ages'].mean()) 
print('\t Generation Count: ', gen3B['Name'].count()) 
print()




##### Gen 1 Second half
# Gen1B
gen1B = treeData['lineage']['Members'][1]
gen1B = pd.json_normalize(gen1B, max_level=20)
gen1B['Ages'] = (gen1B['DeathYear'].astype(int)-gen1B['BirthYear'].astype(int))
print("First Generation")
print(gen1B.sort_values(by = 'Ages')) 
# print(gen1)
print("\t The median age:", gen1B['Ages'].median())
print("\t The mean age:", gen1B['Ages'].mean()) 
print('\t Generation Count: ', gen1B['Name'].count()) 
print()



# Gen1B->Gen2B
gen2B = treeData['lineage']['Members'][1]['Members']
gen2B = pd.json_normalize(gen2B, max_level=20)
gen2B['Ages'] = (gen2B['DeathYear'].astype(int)-gen2B['BirthYear'].astype(int))
print("Second Generation")
print(gen2B.sort_values(by = 'Ages')) 
# print(gen2)
print("\t The median age:", gen2B['Ages'].median())
print("\t The mean age:", gen2B['Ages'].mean()) 
print('\t Generation Count: ', gen2B['Name'].count()) 
print()


# Gen1B->Gen2->Gen3B
gen3C = treeData['lineage']['Members'][1]['Members'][1]['Members']
gen3C = pd.json_normalize(gen3C, max_level=20)
gen3C['Ages'] = (gen3C['DeathYear'].astype(int)-gen3C['BirthYear'].astype(int))
print("Third Generation")
print(gen3C.sort_values(by = 'Ages')) 
# print(gen3B)
print("\t The median age:", gen3C['Ages'].median())
print("\t The mean age:", gen3C['Ages'].mean()) 
print('\t Generation Count: ', gen3C['Name'].count()) 
print()

