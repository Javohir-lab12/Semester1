family_name = input("What is your family name? ")
combined_monthly_income = float(input("What is your comnbined monthly income? "))
mortgage_rent = float(input("How much is your mortage rent ecpences? "))
insurance = float(input("How much is your insurance ecpences? "))
car_payment = float(input("How much is your car payment ecpences? "))
utilities = float(input("How much is your utilities ecpences? "))
groceries = float(input("How much is your grocery expences? "))
childcare = float(input("How much is your childcare expences? "))
family_activities = float(input("How much is your family activities expences? "))
current_vacation_fund_balance = float(input("How much is your current vacation fund balance? "))
vacation_cost = float(input("How much is your vacation cost target? "))
months_until_vacation_date = int(input("How many months do you have until vacation date? "))
fixed_expenses = mortgage_rent + insurance + car_payment + utilities
variable_expenses =groceries + childcare + family_activities 
total_monthly_expenses = fixed_expenses + variable_expenses
monthly_savings_potential = combined_monthly_income - total_monthly_expenses
savings_rate_percentage = ( monthly_savings_potential / combined_monthly_income ) * 100
projected_vacation_fund = current_vacation_fund_balance + ( monthly_savings_potential * months_until_vacation_date )
total_needed = vacation_cost - current_vacation_fund_balance
monthly_savings_needed = total_needed / months_until_vacation_date
monthly_shortfall_or_surpluss = monthly_savings_potential - monthly_savings_needed
total_gap = monthly_shortfall_or_surpluss * months_until_vacation_date
emergency_status = savings_rate_percentage < 10
needs_improvement = savings_rate_percentage >= 10 and savings_rate_percentage < 15
stable = savings_rate_percentage >= 15 and savings_rate_percentage < 25
strong = savings_rate_percentage >= 25
vacation_affordable = projected_vacation_fund >= vacation_cost
print("\n***Family Budjet Planner***")
print(f"Family name: {family_name}")
print("Incomes and expenses:")
print(f" - Family monthly income: ${combined_monthly_income:.2f}")
print(f" - Total monthly expenses: ${total_monthly_expenses:.2f}")
print(f"  - Total fixed expenses: ${fixed_expenses:.2f}")
print(f"   - Mortgage rent: ${mortgage_rent:.2f} ")
print(f"   - Insurance: ${insurance:.2f} ")
print(f"   - Car_payment: ${car_payment:.2f} ")
print(f"   - Utilities: ${utilities:.2f} ")
print(f"  - Total variable ecpences: ${variable_expenses:.2f}")
print(f"   - Groceries: ${groceries:.2f}")
print(f"   - Childcare: ${childcare:.2f}")
print(f"   - Family activities: ${family_activities:.2f}")
print("Savings metrics:")
print(f" - Monthly savings potential: ${monthly_savings_potential:.2f}")
print(f" - Savings rate percentage: {savings_rate_percentage:.2f}%")
print(f" - Current vacation fund: ${current_vacation_fund_balance:.2f}")
print(f" - Projected fund at vacation date: ${projected_vacation_fund:.2f}")
print("Vacation goal analysis: ")
print(f" - Target vacation cost: ${vacation_cost:.2f}")
print(f" - Total amount needed: ${total_needed:.2f}")
print(f" - Monthly savings needed: ${monthly_savings_needed:.2f}")
print(f" - Monthly shortfall/surplus: ${monthly_shortfall_or_surpluss:.2f}")
print("Financial Health Indicators:")
print(f"Emergency status: {emergency_status}")
print(f"Needs improvement: {needs_improvement}")
print(f"Stable: {stable}")
print(f"Strong: {strong}")
print(f"Vacation affordable: {vacation_affordable}")
print(f"Vacation affordability status: {vacation_affordable}")
print(f"Total gap at vacation date: ${total_gap:.2f}")