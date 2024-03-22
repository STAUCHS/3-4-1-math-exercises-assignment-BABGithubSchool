#-------------------------------------------------------------------------
# Name:         Hours
# Purpose:		Lets you enter a number of hours, and converts it to days and hours.
# Author:       Bassias, B
# Created:      22/03/2024
#-------------------------------------------------------------------------
hours = input("Enter the number of hours:")
days = (int(hours)/24)
newhours = (int(hours)%24)
print(hours, "hours =", int(days), "days and", newhours, "hours.")
