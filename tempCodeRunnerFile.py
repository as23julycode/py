name = input("Enter your name: ")
age = int(input("how old are you {0}: " .format(name)))
print(age)

if age > 18:
    print("you are eligible to vote")
elif age == 18:
    print("you are exact")
else:
    print("please come back after {0} year".format(18 - age)) 