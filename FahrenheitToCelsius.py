#-------------------------------------------------------------------------
# Name:         Fahrenheit to Celsius
# Purpose:		Lets the user enter the temperature in Fahrenheit, and prints out the result in Celsius. 
# Author:       Bassias, B
# Created:      22/03/2024
#-------------------------------------------------------------------------
fahren = input("Enter the temperature in fahrenheit:")
celc = ((int(fahren)-32)*5/9)
print(fahren, "degrees fahrenheit is", int(celc), "degrees celcius.")
