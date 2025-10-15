#inputs
family_name = input("What is your fmaily name? ")
combined_monthly_income = float(input("What is your comnbined monthly income? "))
fixed_expenses = float(input("How much is your fixed expences? "))  #Mortgage/rent, insurance, car payment, utilities
variable_expenses = float(input("How much is your variable expenxes? ")) #Groceries, childcare, family activities
current_vacation_fund_balance = float(input("How much is your current vacation fund balance? "))
vacation_cost = float(input("How much is your vacation cost target? "))
months_until_vacation_date = int(input("How many months do oyu have untill vacation date"))
#variabes
total_monthly_expenses = fixed_expenses + variable_expenses
monthly_savings = combined_monthly_income - total_monthly_expenses
savings_rate_percentage = monthly_savings / combined_monthly_income
projected_vacation_fund = current_vacation_fund_balance + monthly_savings 
total_needed = vacation_cost - current_vacation_fund_balance
monthly_savings_needed = total_needed / months_until_vacation_date
monthly_shortfall = monthly_savings - monthly_savings_needed, negative = "Need more"
total_shortfall = monthly_shortfall * months_until_vacation_date
#status indicators
