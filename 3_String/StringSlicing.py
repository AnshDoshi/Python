greeting='good morning'
name=' Ansh'
# concatinating two strings
a=greeting+name
print(a)
print(greeting[0:4])#good(last index does not count)
print(greeting[:4])#good
print(greeting[0:])#fullname
print(greeting[-7:-1])#mornin
print(greeting[-7:])#morning
# Slicing with skip value

# We can provide a skip value as a part of our slice like this:
name=' anshdoshi'
print(name[0:5])#ansh
print(name[0:5:1])#ansh
print(name[1:5:2])#as
print(name[0::2])#nhoh

# word = “amazing”

# word[1:6:2]           # It will return ’mzn’

# word = ‘amazing’

# word[:7] or word[0:7]      #It will return ‘amazing’

# word[0:] or word[0:7]      #It will return ‘amazing’
