# finance calculator
monthly_income = float(input("Enter your monthly income: "))
mothly_expenses = float(input("Enter your total monthly expenses: "))
monthly_savings = float(monthly_income) - float(mothly_expenses)
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

print("Your monthly savings are $" + str(monthly_savings))
print("Projected savings after one year, with interest, is: $" +
      str(projected_savings))
