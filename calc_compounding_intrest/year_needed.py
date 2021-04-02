# estimate years needed to reach saving goal

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
final_amount = 0

if goal < principal or goal == principal:
    years_needed = 0

while final_amount < goal:
    final_amount = (final_amount + yearly_invest) * (1+ interest)
    years_needed += 1

print("You need to safe for", years_needed, "years to have", goal, "bucks on your account.")


