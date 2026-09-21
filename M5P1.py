# Kirill Kaminskyi M5P1.py 9/16/2026

#input quantity
quantity = int(input("Enter quantity of an item: "))

#if statement

if quantity >= 1000:
    unit_price = 3
else:
    unit_price = 5

#process
extended_price = quantity * unit_price
tax = extended_price * 0.07
total = extended_price + tax

#output
print (f"Quantity: {quantity}")
print (f"Price: ${unit_price:,.2f}")
print (f"Extended price: {extended_price:,.2f}$")
print (f"Tax: {tax:,.2f}$")
print (f"Total price: {total:,.2f}$")


