import math

"""
This program enables a user to choose from 2 types of financial calculators,
One will be an investment calculator and the other will be a home loan
repayment calculator.
At the start, the user should see the options available. User prompted to make
a choice. The program will first display the options and ask user for input
to proceed.
If 'investment' is chosen, it takes inputs for principal, interest rate, time, 
and interest type (simple or compound) and calculates and displays the total amount. 
If 'bond' is chosen, it currently prints a placeholder message, but you can add the 
code for bond calculation as needed. Bond part was completed
"""

import math

# Function to calculate simple interest
def calculate_simple_interest(principal, rate, time):
    return principal * (1 + rate * time)

# Function to calculate compound interest
def calculate_compound_interest(principal, rate, time):
    return principal * math.pow((1 + rate), time)

# Function code to calculate bond repayment
def calculate_bond_repayment(principal, annual_rate, months):
    monthly_rate = annual_rate / 100 / 12
    return principal * monthly_rate / (1 - math.pow((1 + monthly_rate), -months))

# Display menu to the user
print("investment - to calculate the amount of interest you'll earn on your investment\n"
      "bond - to calculate the amount you'll have to pay on a home loan")
user_choice = input("Enter either 'investment' or 'bond' from the menu above to proceed: ").lower()

# Check user's choice and proceed accordingly
if user_choice == 'investment':
    # Get input for investment calculation
    principal = float(input("Enter the amount of money you are depositing: "))
    rate = float(input("Enter the interest rate (as a percentage): ")) / 100
    time = int(input("Enter the number of years you plan on investing: "))
    interest_type = input("Enter 'simple' or 'compound' interest: ").lower()

    # Calculate and display the result based on the interest type
    if interest_type == 'simple':
        total_amount = calculate_simple_interest(principal, rate, time)
    elif interest_type == 'compound':
        total_amount = calculate_compound_interest(principal, rate, time)
    else:
        print("Invalid interest type. Please enter 'simple' or 'compound'.")
        total_amount = None

    if total_amount is not None:
        print(f"Total amount after {time} years with {interest_type} interest: {total_amount:.2f}")

elif user_choice == 'bond':
    # Get input for bond calculation
    principal = float(input("Enter the present value of the house: "))
    annual_rate = float(input("Enter the annual interest rate (as a percentage): "))
    months = int(input("Enter the number of months you plan to repay the bond: "))

    # Calculate and display the monthly repayment amount
    monthly_repayment = calculate_bond_repayment(principal, annual_rate, months)
    print(f"Your monthly repayment will be: {monthly_repayment:.2f}")

else:
    print("Invalid choice. Please enter 'investment' or 'bond'.")

