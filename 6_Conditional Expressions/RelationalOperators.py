# Relational operators are used to evaluate conditions inside if statements. Some examples of relational operators are:

# = = -> equals

# >=  -> greater than/equal to

# <=, etc.
# Logical Operators
# In python, logical operators operate on conditional statements. Example:

# and -> true if both operands are true else false

# or -> true if at least one operand is true else false

# not -> inverts true to false and false to true
# elif clause
# elif in python means [else if]. If statement can be chained together with a lot of these elif statements followed by an else statement.

# '''
# if (condition1):
#     #code
# elif (condition 2):
#     #code
# elif (condition 2):
#     #code
# ….
# else:
#     #code    '''
# The above ladder will stop once a condition in an if or elif is met.





age=int(input("what is your age: "))
if(age>21 and age<60):
    print("you can work with us..")
else:
    print("you cant work with us..")