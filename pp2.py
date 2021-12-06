# python practice problem 2
# divide the apples
# harry potter has got a number of apples .harry has some students among
#  whom,he wants to distribute the apples.
#  these n number of apples are provided to harry by his friends and he can request for
#  few more or few less apples.
#  you need to print a number in range mn to mx is a divisor of n or not
#  input:
#  take input n,mn,and mx from the user
#  output:
#  print whether the numbers between mn and mx are divisor of n or not
#  if mn = mx , show that this is not a range and mn is equal to mx.
#  show the result for that number
#  example:
#  if n is 20 and mn =2 and mx = 5
#  2 is a divisor of 2050

#  3 is not a divisor of 20
#  4 is not a divisor of 20
#  5 is not a divisor of 20

# SOLUTION:-

apples = int(input("Enter the numbers of apples\n"))
mn = int(input("Enter the minimum number to check \n"))
mx = int(input("Enter the maximum number to check \n"))

for i in range(mn, mx + 1):
    if apples % i == 0:
        print(f"{i} is a divisor of {apples}")
    else:
        print(f"{i} is not a divisor of {apples}")

