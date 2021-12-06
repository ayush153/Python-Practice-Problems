# Python practice problem 1
# Your age in 2090
# Take age or input from the user and tell them when will they turn 100 years old.
# Don't use any modulelike datetime or dateutils.
# They can then provide a year and your program must tell their age in that
#  particular year.
# You should be handling all sorts of errors like:
# . YOU are not yet born
# .You seem to be the oldest person alive
# .You can also handle any other error if possible!

# SOLUTION:-

yearAge = int(input("What is your Age/Year of birth\n"))
isAge = False
isYear = False

if len(str(yearAge)) == 4:
    isYear = True

else:
    isAge = True

if(yearAge<1900 and isYear):
    print("You seem to be the oldest person alive")
    exit()

if(yearAge>2019):
    print("You are not yet born")
    exit()

if isAge:
    yearAge = 2019 - yearAge  

print(f"You will be 100 years old in {yearAge + 100}")

interestedYear = int(input("Enter the year you want to know your age in\n"))

print(f"You will be {interestedYear - yearAge} years old in {interestedYear}")

