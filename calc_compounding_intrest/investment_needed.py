#estimate investment

print("How many years will you be saving?")
years = int(input("Enter years: "))

print("How much money is currently on your account?")
principal = float(input("Enter current amount in account: "))

print("What are your yearly interests of this investment?")
interest = float(input("Enter interest in decimal numbers (10% = 0.1): "))

print("How much money do you want to reach?")
goal = float(input("Enter amount: "))

yearly_investment = (goal - principal - (years * interest)) / (years * years)
monthly_investment = yearly_investment / 12

print("You need to invest", monthly_investment, "per month to have a credit of", goal, "after", years, "years.")
