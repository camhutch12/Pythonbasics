for i in range(1, 20):  # looks like a for (int i=1; i<19; i++)
    print("i is now {}".format(i))

number = "9,223,372,036,854,775,807"
for i in range(0, len(number)):
    print(number[i])

number = "9,223,372,036,854,775,807"
cleanNumber = " "
for i in range(0, len(number)):
    if number[i] in '0123456789':
        cleanNumber += number[i]
newNumber = int(cleanNumber)
print("the number is {} ".format(newNumber))
