import math
interest = 0

#Task: a program that allows the user to access two different financial calculators: an investment calculator and a home loan repayment calculator.
 
#Objective: Ask the user to choose which calculation they want to do between an investment and bond calculation
calculation_type = input("Would you like to do a bond or investment calculation?: ")

#Prompt the user for input if they choose investment

#Objective2: process when the user chooses investment or bond
if  calculation_type.upper() == "INVESTMENT":
    money_amount = float(input("How much money are you depositing?: ")) 
    interest_rate = float(input("How much percentage of interest should be applied?: ")) 
    years_investing = float(input("How many years do you plan on investing for?: "))
    interest = input("Would you like simple or compound interest?: ")

#If the user chooses interest the program will calculate and print the amount  
    if interest.upper() == "SIMPLE" :
        interest_calculation = interest_rate/int(100)
        simple_investment_total = (money_amount) * (1 + (interest_calculation) * (years_investing))
        print(simple_investment_total)
    elif interest.upper() == "COMPOUND" :
        interest_calculation = interest_rate/int(100)
        compound_investment_total = (money_amount) * (math.pow((int(1) + (interest_calculation)), (years_investing)))
        print(compound_investment_total)

#If the user chooses bond the program will calculate how much and print the amount
elif calculation_type.upper() == "BOND" :
    house_value = float(input("What is the current value of the house?: ")) #Prompt the user for input if they choose bond
    interest_rate_house = float(input("What is the interest rate?: "))
    months_repayment = float(input("How many months do you wish to take in order to repay the bond?: "))
    interest_rate_house_calculation = interest_rate_house/int(100) / 12
    bond_total = (house_value * interest_rate_house_calculation) / (1 - math.pow((int(1) + interest_rate_house_calculation), - months_repayment))
    print("You will need to pay " + str(bond_total) + " per month.")