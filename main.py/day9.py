#This file was created by Logan Azzolina
#python conditions and if statements 
#A while loop that says "bueller" 10 times fast 
#A for loop that says "Anyone" 5 times then breaks.
#A conditional statement that calls a function.

#create the while loop

# b = 1
# c = "bueller""
# while b < 11:
#     print

#fromw3schools
# i = 1
# while i < 6:
#   print(i)
#   i += 1

#   #done with the break function 

#   d = 0
#   e = "Bueller"
#   while d < 10:
#     print(e)
#     if d == 10:
#       break
#     d + 1

#     # create the loop with the break function "anyone"

#     f = 1
#     g = "anyone"



#     while f < 6:
#       print(g)
#       f += 1 
#       print("function end")
#       break

# following along with teacher 

from time import sleep

from random import randint


x = 1




while x < 10:
    print('bueller')
    print(x)
    #sleep(2)
    x += 1
hps = 100

enemies = ["Bob", "Tom", "Bill"]

for i in enemies:
    print(i)

def myFunc(greeting):
    name = input("give me name:")
    print(greeting + name)

askingforname = True

if askingforname:
    myFunc("Hello there....")


    
