import math

#General information key, new line to space out information so it's easer to read 
print("FINANCE CALCULATOR")
print("\nInvestment:  to calculate the amount of interest you'll earn on your investment")
print("Bond:        to calculate the amount you'll have to pay on a home loan")

#Asking the customer to input either investment or bond, answer is stored in the variable 'choice'
#Input is converted to all uppercase 
choice = (input("\nPlease enter either 'investment' or 'bond' to proceed:")).upper()

#Print choice that the user has entered 
print(f"\nYou have chosen {choice}")

# If user inputs 'investment', programme prompts them to enter deposit amount, interest rate, length of investment 
# These are converted to floats to enable the data to be used in calculations
# After entering the numbers, prompts user to enter type of interest 
if choice == "INVESTMENT":
    deposit = float(input("Enter amount to deposit in pounds(£): ")) 
    interest_rate = float(input("Enter interest rate(%): "))
    num_of_years = float(input("Enter number of years you plan on investing: "))
    interest_type = input("Please choose either 'simple' or 'compound' interest: ")

    #Within the first if statement, depending on whether compound or simple was entered, these are the 2 equations
    #If compount entered - variables entered into the compound interest equation and rounded up to 2 decimal places 
    #Then print statement summarizing the data entered and final result of calculation 
    if interest_type == "compound" or interest_type == "Compound": 
        compound_interest = round((deposit *math.pow((1+(interest_rate/100)),num_of_years)),2)
        print(f"\nSUMMARY:\nDeposit: £{deposit}\nInterest rate: {interest_rate}%\nLength of investment (years): {num_of_years}")
        print(f"Your final amount with COMPOUND interest will be £{compound_interest}")

    #Else if simple entered - variables entered into the simple interest equation and rounded to 2 decimals
    #Then print summary of values and statement of total interest
    elif interest_type == "simple" or interest_type == "Simple":
        simple_interest = round((deposit*(1+(interest_rate/100)*num_of_years)),2)
        print(f"\nSUMMARY:\nDeposit: £{deposit}\nInterest rate: {interest_rate}%\nLength of investment (years): {num_of_years}")
        print(f"Your total amount with SIMPLE interest will be £{simple_interest}")

#If user inputed 'bond' into the choice variable, prompts input for variables as listed 
#Values converted to float to enable calculations later 
elif choice == "BOND":
    present_value = float(input("Please enter current value of your property in pounds(£): "))
    bond_interest_rate = float(input("Please enter interest rate(%): "))
    length_of_bond = float(input("Please enter the number of months to repay the bond: "))
#Equation to calculate repayment per month with variables inserted 
    repayment = ((bond_interest_rate/1200)*present_value)/(1-(1+(bond_interest_rate/1200))**(-length_of_bond))
#Repayment figure rounded to 2 decimals and saved in new variable 
    repayment_rounded = round(repayment, 2)
#Print summary statement of values entered and final statement of the repayment figure 
    print(f"\nSUMMARY:\nValue of current loan: {present_value}\nInterest rate(%): {bond_interest_rate}\nTime to repay bond(months): {length_of_bond}")
    print(f"You will need to pay £{repayment_rounded} per month to repay your debt.")