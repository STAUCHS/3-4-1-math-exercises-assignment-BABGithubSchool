#-------------------------------------------------------------------------
# Name:         Volume of a Cone
# Purpose:		Computes the volume of a cone given the radius and height from the user.
# Author:       Bassias, B
# Created:      22/03/2024
#-------------------------------------------------------------------------
import math
radius = input("Enter the radius (cm):")
height = input("Enter the height (cm):")
volume = round((math.pi*(int(radius)**2)*int(height)/3), 1)
print("The volume of your cone is", volume, "cm^3.")