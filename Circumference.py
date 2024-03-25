#-------------------------------------------------------------------------
# Name:         Circumference
# Purpose:		Calculates the circumference of a circle using a radius given by the user.
# Author:       Bassias, B
# Created:      22/03/2024
#-------------------------------------------------------------------------
import math
radius = input("Enter the radius (cm):")
circum = round((float(radius)*math.pi*2), 2)
print ("The circumference of your circle is", float(circum), "cm^2")