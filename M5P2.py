# Kirill Kaminskyi M5P2.py 9/21/2026

#input

item_name = input("Enter item: ")
item_quantity = int(input("Enter quantity of an item: "))

#process
A = 10
B = 20

if item_name == "A":
    unit_price = A
else:
    unit_price = B

extended_price = unit_price * item_quantity

#output
print (f"Item: {item_name}")
print (f"Unit price: ${unit_price:,.2f}")
print (f"Extended price: {extended_price:,.2f}")


