# Kirill Kaminskyi M5P2.py 9/21/2026

#input
last_name = input("Enter last name: ")
num_of_dependents = int(input("Enter number of dependents: "))
gross_income = float(input("Enter you gross income: "))

#process
adjusted_gross_income = gross_income - (num_of_dependents * 12000)

if adjusted_gross_income > 50000:
    tax_rate = 0.20
else:
    tax_rate = 0.10

income_tax = adjusted_gross_income * tax_rate

if income_tax < 0:
    income_tax = 100

#output
print (f"Last name: {last_name}")
print (f"Gross income: ${gross_income:,.2f}")
print (f"Number of dependents:  {num_of_dependents}")
print (f"Adjusted gross income: ${adjusted_gross_income:,.2f} ")
print (f"Income tax: ${income_tax:,.2f}")