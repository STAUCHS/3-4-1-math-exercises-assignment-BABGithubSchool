#-------------------------------------------------------------------------
# Name:         Minutes
# Purpose:		Lets you enter a number of minutes, and converts it to days, hours, and minutes.
# Author:       Bassias, B
# Created:      22/03/2024
#-------------------------------------------------------------------------
minutes = input("Enter the number of minutes:")
newminutes = (int(minutes)%60)
hours = (int(minutes)/60)
days = (int(hours)/24)
newhours = (int(hours)%24)
print(minutes, "minutes =", int(days), "days,", newhours, "hours, and", newminutes, "minutes")