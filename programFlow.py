# name = input("please enter your name")
# age = int(input("how are you {}".format(name)))
# print(age)
#
# if age>=18:
#     print("you are old enough to vote")
#     print("please put an x in the box")
# else:
#     print("please come back in {} years".format(18-age))

print("please guess a number between 1 and 10")
guess = int(input())

if guess < 5:
    print("guess higher")
    guess = int(input())
    if guess == 5:
        print("great you guessed it ")
    else:
        print("sorry, you have not guessed correctly")

elif guess > 5:
    print("please guess lower")
    guess=(int(input()))
    if guess==5:
        print("well done. you guessed it")
    else:
        print("sorry you have not guessed correctly")

else:
    print("you got it first try")
