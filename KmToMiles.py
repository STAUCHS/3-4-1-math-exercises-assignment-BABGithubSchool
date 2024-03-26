#-------------------------------------------------------------------------
# Name:         Km to Miles
# Purpose:		Converts a distance in kilometers into miles.
# Author:       Bassias, B
# Created:      22/03/2024
#-------------------------------------------------------------------------
km = input("Enter the distance in km:")
miles = round((int(km)*0.621371), 2)
print(km, "km is", miles, "miles.")
print(str(km) + "km is" + str(miles) + " miles.")
print(f"{km} km is {miles} miles.")
