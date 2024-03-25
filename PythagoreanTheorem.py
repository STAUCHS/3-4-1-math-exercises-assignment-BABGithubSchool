#-------------------------------------------------------------------------
# Name:         Pythagorean Theorem
# Purpose:		Takes the lengths of the two legs of a right-angle triangle from the user and apply the Pythagorean Theorem to find the hypotenuse.
# Author:       Bassias, B
# Created:      22/03/2024
#-------------------------------------------------------------------------
a = input("Enter the length of side a:")
b = input("Enter the length of side b:")
c = round((((int(a)**2)+(int(b)**2))**0.5), 1)
print("The hypotenuse of a right triangle with legs", a, "and", b, "is", c, "units.")