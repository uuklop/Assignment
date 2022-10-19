
''' firstAssignment

    *
    **
    ***
    *****

    *************
    *           *
    *           *
    *           *
    *************

    *********
    *******
    *****
    ***
    **
    *


'''
number = int(input("Enter a Number: "))

# Loop For Triangle
print("\nInverted Triangle Pattern\n")
for row in range(number):
    for column in range(number-row):
        print("*", end="")
    print()


print()
# Loop For Inverted Triangle
print("\nTriangle Pattern\n")
for row in range(number):
    for column in range(row):
        print("*", end='')
    print()



# Loop For Square
print("\nSquare Pattern \n")
for row in range(number):
    for column in range(number):
        if row == 0 or row == number - 1 or column == 0 or column == number - 1:
            print("* ", end="")
        else:
            print("  ",end="")
    print()