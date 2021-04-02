#select calculator
print("1: estimate monthly investment needed")
print("2: estimate years needed")
print("3 estimate credit after certain years and certain amount of invest")
calculator = int(input("calculator 1, 2 or 3: "))

#estimate investment
if calculator == 1:
    print("How many years will you be saving?")
    years = int(input("Enter years: "))

    print("How much money is currently on your account?")
    principal = float(input("Enter current amount in account: "))

    print("What are your yearly interests of this investment?")
    interest = float(input("Enter interest in decimal numbers (10% = 0.1): "))

    print("How much money do you want to reach?")
    goal = int(input("Enter rounded amount (50.05 --> 50): "))

    
    for i in range(0, goal):
        invest_yearly = i
        for i in range(0, years):
            principal = (principal + invest_yearly) * (1+ interest)
        if principal == goal:
            #monthly_invest = invest_yearly / 12
            break
        else:
            continue
    monthly_invest = invest_yearly / 12
    print("You need to invest", monthly_invest, "per month to have a credit of", goal, "after", years, "years.")

#estimate years
elif calculator == 2:
    print("How much money do you want to reach?")
    goal = float(input("Enter amount: "))

    print("How much money is currently in your account?")
    principal = float(input("Enter current amount in account: "))

    print("How much money do you plan on investing monthly?")
    monthly_invest = float(input("Enter amount: "))

    print("What do you estimate will be the yearly interest of this investment?")
    interest = float(input("Enter in decimal numbers (10% = 0.1): "))

    print("")

    yearly_invest = monthly_invest * 12
    years_needed = 0
    money_to_safe = (goal - principal)
    
    if goal < principal or goal == principal:
        years_needed = 0

    while principal < goal:
        principal = (principal + yearly_invest) * (1+ interest)
        years_needed += 1

    print("You need to safe for", years_needed, "years to have", goal, "bucks on your account.")

#estimate credit
elif calculator == 3:
    print("How many years will you be saving?")
    years = int(input("Enter years: "))

    print("How much money is currently in your account?")
    principal = float(input('Enter current amount in account:'))

    print('How much money do you plan on investing monthly')
    monthly_invest = float(input("Enter amount: "))

    print("What do you estimate will be the yearly interest of this investment?")
    interest = float(input("Enter interest in decimal numbers (10% = 0.1): "))

    print("")

    monthly_invest = monthly_invest * 12
    final_amount = 0

    for i in range(0, years):
        if final_amount == 0:
            final_amount = principal

        final_amount = (final_amount + monthly_invest) * (1+ interest)

    print("This is how much money you would have in your account after", years, "years: ", final_amount)

else:
    print("invalid input, restart program")
