# Sometimes we want to play pubg on our phone if the day is Sunday.

# Sometimes we order Ice-cream online if the day is sunny.

# Sometimes we go hiking if our parents allow.

# All these are decisions that depend on the condition being met.

# In python programming too, we must be able to execute instructions on a condition(s) being met. This is what conditions are for!

# If else and elif in Python
# If else and elif statements are a multiway decision taken by our program due to certain conditions in our code.

# Syntax:

# '''
# if (condition1):		// if condition 1 is true
# 	print(“yes”)
# elif (condition2):		// if condition 2 is true
# 	print(“No”)
# else:				// otherwise
# 	print(“May be”)
# '''


# Code example:

# a = 22
# if (a>9):
#     print(“Greater”)
# else:
#     print(“lesser”)




#elif ladder
a = 7
if(a < 3):
         print("less than 3")
elif(a > 7):
        print("greater than 7")

else:
        print("greter than 3 or less than or equal to 7")


#Multiple if statements

b = 2
if(b < 3):
         print("less than 3")
if(b > 7):
        print("greater than 7")

else:
        print("greter than 3 or less than or equal to 7")

#age programm
age=int(input("what is your age: "))

if(age>18):
        print("you are eligible")
else:
        print("your not eligible")