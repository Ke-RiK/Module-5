# Kirill Kaminskyi M5P2.py 9/21/2026

#input
number_of_books = int(input("Enter number of books: "))
cost_per_book = float(input("Enter cost of books: "))

#process
order_total = number_of_books * cost_per_book

if order_total <= 50:
    order_total += 25
    shipping_cost = 25
else:
    order_total += 0
    shipping_cost = 0
#output
print (f"Order total: ${order_total:,.2f}")
print (f"Shipping cost: ${shipping_cost}")