import math 

print("Welcome to your investment and bond calculator! \n")

print("Investment - to calculate the amount of interest you'll earn on your investment.")
print("Bond - to calculate the amount you'll have to pay on a home loan. \n")

# Prompts the user for input to perform the next block of code.
selection = input("Enter either 'investment' or 'bond' from the menu above to proceed: ").lower() # .lower() fixes inputs case sensitivity and crashing the code.
print("\n")

# This ensures the input repeats in the case that the users input is incorrect.
while selection != "investment" and selection != "bond":
    selection = input("Invalid response, Please re-enter either 'investment' or 'bond': ").lower()
    print("\n")

if selection == "investment": # if condition for input as 'investment'.
    print("Investment: \n")

    deposit = input("How much money are you investing (£): ").replace(",","")

    while deposit.isalpha(): # if the user enters an alphabetic character it asks for the input again.
        print("\n")
        deposit = input("Invalid response, Please enter how much money you are investing (£): ").replace(",","")
        print("\n")

    interest_rate = (input("Please enter the current interest rate (%): "))

    while interest_rate.isalpha(): # if the user enters an alphabetic character it asks for the input again.
        print("\n")
        interest_rate = input("Invalid response, Please enter the current interest rate (%): ")
        print("\n")

    years = (input("Please enter amount of years you would like to invest (in numbers): "))
    print("\n")

    while years.isalpha(): # if the user enters an alphabetic character it asks for the input again.
        print("\n")
        years = input("Invalid response, Please enter amount of years you would like to invest (in numbers): ")
        print("\n")
    
    interest = input("Please enter whether you want 'simple' or 'compound' interest: ").lower()
    print("\n")

    r = float(interest_rate) / 100 # casting and setting the varaibles to calulate the simple and compound interest.
    p = float(deposit)
    t = float(years)
     
    while interest != "simple" and interest != "compound":
        interest = input("Invalid response, Please re-enter either 'simple' or 'compound': ").lower()
        print("\n")

    if interest == "simple": 
        a = (p * (1 + r * t))
        a = round(a,2) # round() is set to round to the 2nd decimal place
        a = str(f"{a:,}")
        print("Your total amount after investment is £" + a)
        print("\n")

    elif interest == "compound":
        a = (p * math.pow((1 + r), t))
        a = round(a,2) # round() is set to round to the 2nd decimal place
        a = str(f"{a:,}")
        print("Your total amount after investment is £" + a)
        print("\n")

if selection == "bond": # if condition for input as 'bond'.
    print("Bond: \n")

    value = input("Please enter the current value of your house (£): ").replace(",","")

    while value.isalpha(): # if the user enters an alphabetic character it asks for the input again.
        print("\n")
        value = input("Invalid response, Please enter the current value of your house (£): ").replace(",","")
        print("\n")

    house_interest_rate = input("Please enter the current interest rate (%): ")

    while house_interest_rate.isalpha(): # if the user enters an alphabetic character it asks for the input again.
        print("\n")
        house_interest_rate = input("Invalid response, Please enter the current interest rate (%): ")
        print("\n")

    months = input("Please enter amount of months you plan on taking to repay the bond: ")
    print("\n")
    
    while months.isalpha(): # if the user enters an alphabetic character it asks for the input again.
        print("\n")
        months = input("Invalid response, Please enter amount of months you plan on taking to repay the bond: ")
        print("\n")

    p = float(value) # casting and setting the varaibles to calulate the bond repayment.
    i = (float(house_interest_rate) / 100) / 12
    n = float(months)

    r = (i * p) / (1 - (1 + i) ** (-n))
    r = round(r,2)
    r = str(f"{r:,}")
    print("The amount you will have to repay on your home loan a month is £" + r)
    print("\n")