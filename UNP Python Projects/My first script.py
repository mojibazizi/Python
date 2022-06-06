#define and set variables from user input (casted to a float )
bill = float(input("How much is the meal?"))
tax = float(input("what is the sale's tax (percentage)?"))
tip = float(input("how much of a tip (percentage)?"))

#calculate and add tax
tax_amount = (bill + tax) / 100 #calculate the tax
total = bill + tax_amount #add tax amount to final bill

#calculate and add tip
tip_amount = (total * tip) / 100 #calculate the tip amount
total = total + tip_amount #add tip to final bill


#round the total to 2 decimal places
total + round(total, 2) #round the total to 2 decimal places

#print the final amount
print("The total bill is $",total , sep = '' )
