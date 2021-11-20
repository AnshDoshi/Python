l1=[1,5,3,2,6,20,10]
print(l1)#[1, 5, 3, 2, 6, 20, 10]

l1.sort()
print(l1)#[1, 2, 3, 5, 6, 10, 20]

l1.append(1010)
l1.append(101)
print(l1)#[1, 2, 3, 5, 6, 10, 20, 1010, 101]

l1.insert(0,10)
l1.insert(3,101010)
print(l1)#[10, 1, 2, 101010, 3, 5, 6, 10, 20, 1010, 101]

l1.pop(1)
print(l1)#[10, 2, 101010, 3, 5, 6, 10, 20, 1010, 101]

l1.remove(10)
print(l1)#[2, 101010, 3, 5, 6, 10, 20, 1010, 101]

# L1 = [1, 8, 7, 2, 21, 15]
# sort() – updates the list to [1,2,7,8,15,21]
# reverse() – updates the list to [15,21,2,7,8,1]
# append(8) – adds 8 at the end of the list
# insert(3,8) – This will add 8 at 3 index
# pop(2) – It will delete the element at index 2 and return its value
# remove(21) – It will remove 21 from the last