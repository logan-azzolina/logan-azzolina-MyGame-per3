# file created by Logan Azzolina

# funtion that takes names from terminal 
# puts them in list - list = []
# then spits them in random selection from the list 



import random 

# write a function that randomly selects from user input via append list
def functions():
    mylist = []
    x = input("message")
    mylist.append(x)
    print(x)
    y = input("message")
    mylist.append(y)
    z = input ("message")
    mylist.append(z)
    print(z)
    print("i chose you,", random.choice(mylist))
    return random.choice(mylist)

#return is the last thing a function does
