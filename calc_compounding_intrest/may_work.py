print("How many years will you be saving?")
years = int(input("Enter years: "))

print("How much money is currently in your account?")
principal = float(input('Enter current amount in account:'))

print("What do you estimate will be the yearly interest of this investment?")
interest = float(input("Enter interest in decimal numbers (10% = 0.1): "))

print("Whats your goal?")
goal = int(input("Enter goal: "))

yearly_invest = 0

if years == 1:
    yearly_invest = goal - principal
    final_amount = goal
else:
    for i in range(0,goal):
        yearly_invest = i 
        final_amount = principal
        for x in range(0, years): 
            final_amount = (final_amount + yearly_invest) * (1+ interest)
        if goal < final_amount:
            break
        else:
            continue


monthly_invest = yearly_invest / 12

print(f"monthly investment: {monthly_invest}")
print(f"account: {final_amount}")

print(f"This is how much money you would have in your account after {years} years: {final_amount}")
