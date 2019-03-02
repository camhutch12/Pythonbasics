age = 24
print("my age is " + str(age) + " years")

print("my age is {0} years".format(age))


for i in range(1,12):
    print("No. %2d sqaured is %4d and cubed is %4d " %(i, i**2, i**3)) # not used in python 3

print("\n pi is approxiamtly %12.50f \n\n" % (22/7)) # not used in python3


for i in range(1,12):
    print("No. {0:2} sqaured is {1:<4} and cubed is {2:<4} ".format(i, i**2, i**3))

print("\n pi is approxiamtly {0:12.50} \n\n" % (22/7)) # not used in python3

for i in range(1,12):
    print("No. {} sqaured is {} and cubed is {:4} ".format(i, i**2, i**3))


