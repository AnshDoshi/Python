# 

# ''' a = {“key”: “value”,
# “harry”: “code”,
# “marks” : “100”,
# “list”: [1,2,9]}
# a[“key”]	# Prints value
# a[“list”] 	# Prints [1,2,9] '''


myDict={
    "Fast":"what is not slow",
    "Ansh":"Blockhain Developer",
    "Mark" : [1,101,10],
    "anotherDict":{'ansh':'doshi'}
}


print(myDict['Fast']) # what is not slow

print(myDict['Ansh'])# Blockhain Developer

print(myDict['Mark']) # [1, 101, 10]
myDict['Mark']=[30,10]
print(myDict['Mark']) #[30, 10]

print(myDict['anotherDict']['ansh']) # doshi

# Properties of Python Dictionaries
# It is unordered
# It is mutable
# It is indexed
# It cannot contain duplicate keys

print(type(myDict.keys())) #<class 'dict_keys'>

print((myDict.keys()))  #dict_keys(['Fast', 'Ansh', 'Mark', 'anotherDict'])

print((myDict.values())) #dict_values(['what is not slow', 'Blockhain Developer', [30, 10], {'ansh': 'doshi'}])

print((myDict.items())) #dict_items([('Fast', 'what is not slow'), ('Ansh', 'Blockhain Developer'), ('Mark', [30, 10]), ('anotherDict', {'ansh': 'doshi'})])

updateDict={
    'lotus':'flower',
    'apple':'fruit',
        "Ansh":"Trader",
}
print(updateDict)#{'lotus': 'flower', 'apple': 'fruit', 'Ansh': 'Trader'}
myDict.update(updateDict)
print(myDict)#{'Fast': 'what is not slow', 'Ansh': 'Trader', 'Mark': [30, 10], 'anotherDict': {'ansh': 'doshi'}, 'lotus': 'flower', 'apple': 'fruit'}

#differnce between .get and [] syntax in dictionary
print(myDict.get('Ansh2'))#returns none as Ansh2 is not present in the dictionary
print(myDict['Ansh2'])#throw error because Ansh2 is not the dictionary


# a = {“name”: “ansh”,
# 	“from”: “India”,
# 	“marks”: [92,98,96]}
# items() : returns a list of (key,value) tuple.
# keys() : returns a list containing dictionary’s keys.
# update({“friend”: “Sam”}) : updates the dictionary with supplied key-value pairs.
# get(“name”) : returns the value of the specified keys (and value is returned e.g., "ansh” is returned here)