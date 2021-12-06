# python practice problem 3
# foods and calories
# you visit a resturant called codewithharry and food items in the resturant are sorted 
# based on their amount of calories.
# you have to reverse this list of food items containing their calories.
# you have to use following three methods to reverse a list:-
# . inbuilt method of python
# .listname[::-1]slicing trick
# .swappimg first element with last one and second element with second last one and so on....
# .  6 7 8 34 5 \/ 5 34 8 7 6
# input:
# take a list as an input from the user [5,4,1]
# output:
# [1,4,5]
# [1,4,5]
# [1,4,5]
# all the three methods give same results.

# SOLUTION:-

# Take the size of the list from the user
print("Enter the numbers of the list one by one\n")
size = int(input("Enter size of list\n"))

# Initialize a blank list
mylist = []

# Take the input from the user one by one
for i in range(size):
    mylist.append(int(input("Enter list element\n")))

print(f"Your list is {mylist}\n")

reverse1 = mylist[:]
reverse1.reverse()
reverse2 = mylist[::-1]
print(f"My first reversed list of {mylist} is {reverse1}\n ")
print(f"My second reversed list of {mylist} is {reverse2}\n ")

reverse3 = mylist[:]
for i in range(len(reverse3)//2):
    reverse3[i],reverse3[len(reverse3) -i -1] = reverse3[len(reverse3) -i -1] ,reverse3[i]

# print(f"the reversed list at i = {i} is {reverse3}")
print(f"My Third reversed list of {mylist} is {reverse3}\n ")
if reverse1 == reverse2 and reverse2 == reverse3:
    print("All three methods give same result\n")