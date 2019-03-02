# Write a small program to ask for a name and an age.
# When both values have been entered, check if the person
# is the right age to go on an 18-30 holiday (they must be
# over 18 and under 31).
# If they are, welcome them to the holiday, otherwise print
# a (polite) message refusing them entry.

name = input("please enter you name")
age = int(input("please enter your age"))

if (age<31) and (age>=18):
    print("Welcome {} to the holiday".format(name))

else:
    print("I am sorry you do not meet the age requirements")