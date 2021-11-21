#important:this syntaxwill create an empty dictionaryand not empty set
b={}
print(type(b)) #<class 'dict'>

# S= Set()          # No repetition allowed!

# S.add(1)

# S.add(2)

# # or Set = {1,2}
# If you are a programming beginner without much knowledge of mathematical operations on sets, you can simply look at sets in python as data types containing unique values.
# ties of Sets
# Sets are unordered # Elements order doesn’t matter
# Sets are unindexed # Cannot access elements by index
# There is no way to change items in sets
# Sets cannot contain duplicate valuesProper

#creating an empty set
c=set()
print(type(c))#<class 'set'>

#adding value to empty set
c.add(4)
c.add(5)
c.add(4)
c.add((1,2,3))
#cannot add list or dictionaryto sets
print(c)#{(1, 2, 3), 4, 5}


print(len(c))#3
c.remove(4)
print(c)#{(1, 2, 3), 5}

print(c.pop())#(1, 2, 3)#delete random value
print(c)#{5}


# S = {1,8,2,3}
# Len(s) : Returns 4, the length of the set
# remove(8) : Updates the set S and removes 8 from S
# pop() : Removes an arbitrary element from the set and returns the element removed.
# clear() : Empties the set S
# union({8, 11}) : Returns a new set with all items from both sets. #{1,8,2,3,11}
# intersection({8, 11}) : Returns a set which contains only items in both sets. #{8}



#below code throw error bt you can clear your concepts
# S = Set()

# S.add(20)

# S.add(20.0)

# # S.add(“20”)

# print(len(s))#2
