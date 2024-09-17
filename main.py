# Read the README for instructions.
# You must write an algorithm and test cases first!
#this program calculates and total gas price
#prompt the use to enter miles driven

Miles_str=input("Enter Miles: ")
miles_int=int(Miles_str)

#prompt the user to enter MPG
MPG_str=input("Enter MPG: ")
MPG_int=int(MPG_str)

#prom-pt the user to enter PPG
PPG_str=input("Enter PPG: ")
PPG_int=int(PPG_str)

#calculate miles per gallon

Cost=miles_int/MPG_int*PPG_int

#display cost
print("Your cost per gallon is:" , Cost)
