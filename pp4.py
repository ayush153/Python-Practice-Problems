# python practice problem 4
# the next palindrome
# A palindrome is a string when reversed is equal to itself:
# Examples of palindrome includes 616,mom,madam,676.
# You have to take a number as an input from the user.
# you have to find the next palindrome corresponding to that number.
# your first input be should be number of test cases and 
# then take all the cases as input from the user
# input:
# 3
# 451
# 10
# 2133
# output:
# next palindrome for 451 is 454
# next palindrome for 10 is 11
# next palindrome for 2133 is 2222

# SOLUTION:-

def next_palindrome(n):
    n = n+1
    while not is_palindrome(n):
        n += 1
    return n


def is_palindrome(n):
    return str(n) == str(n)[::-1]


if __name__ == "__main__":
    n = int(input("Enter the number of test cases\n"))
    numbers = []
    for i in range(n):
        number = int(input("Enter the number:\n"))
        numbers.append(number)

    for i in range(n):
        print(
            f"Next palindrome for {numbers[i]} is {next_palindrome(numbers[i])}")

