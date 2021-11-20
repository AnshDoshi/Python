pakau='what is the lenght of this pakau string'
#srtring function

# len() function : It returns the length of the string.
# len(‘ansh’)               #Returns 4
print(len(pakau))

# endswith(“nsh”) : This function tells whether the variable string ends with the string “nsh” or not.
#  If string is “ansh”,
#  it returns for “nsh” since ansh ends with rry.
print(pakau.endswith('string'))#True

# count(“c”) : It counts the total number of occurrences of any character and srirng also
print(pakau.count('a'))  #3
print(pakau.count("what"))  #1

# capitalize() : This function capitalizes the first character of a given string.
print(pakau.capitalize())  #What is the lenght of this pakau string

# find(word) : This function finds a word and returns the index of first occurrence of that word in the string.
print(pakau.find('what'))  #0
# returns the index of only first occurrence

# replace(oldword, newword) : This function replaces the old word with the new word in the entire string.

print(pakau.replace('what','whatt'))
# in the entire string











