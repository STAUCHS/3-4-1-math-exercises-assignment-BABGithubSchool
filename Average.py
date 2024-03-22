#-------------------------------------------------------------------------
# Name:         Average
# Purpose:		Calculates the average of a student's marks.
# Author:       Bassias. Blake
# Created:      22/03/2024
#-------------------------------------------------------------------------
course1 = float(input("What is your grade for course one?"))
course2 = float(input("What is your grade for course two?"))
course3 = float(input("What is your grade for course three?"))
course4 = float(input("What is your grade for course four?"))
average = ((course1+course2+course3+course4)/4)
average = round(float(average))
print("Your grade average is", average, "%.")
