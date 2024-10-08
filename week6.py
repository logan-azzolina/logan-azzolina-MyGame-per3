#this file was created by logan azzolina

# This file was created by logan azzolina

'''
Algorithm for how to build grilled chease sandwhich

1. select chease from fridge
2. select bread from data fridge
3. select grilled type from drawer 
4. take two bread 
5. take one chease 
6. place chease in between bread
7. place cheese sandwhich on grilled type

'''
#counting by twos 
#there is an odd number of occupants
#Assumptions - we know number of people in the room
# N = 0
# people_in_room = 3

# #loop that counts by two until N is equal to number of people in room
# while N <  people_in_room:
#     N += 2
#     # if the difference is one (meaning odd) then add one at a time....
#     if people_in_room - N == 1:
#         N + 1
#     print(N)
   

level1 = ["hello"
          "world",
          "thing",
          "pasta",
                ]

for row in level1:
    print(row)
    for col in row:
        print(col)


print(list(enumerate(level1)))

'''
This best sorting algorithm in python is merge sort 
a divide-and-conquer algorithm that divides the list into halves, sorts them, and merges them.
sources: https://www.geeksforgeeks.org/merge-sort/?ref=shm
         https://coderslegacy.com/python/merge-sort-algorithm/

'''