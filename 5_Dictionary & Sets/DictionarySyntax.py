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

