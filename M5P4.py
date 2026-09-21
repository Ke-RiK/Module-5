# Kirill Kaminskyi M5P2.py 9/21/2026

#input
name_appliances = input("Enter name of appliances: ")
cost_appliances = float(input("Enter cost appliances: "))

#process

if cost_appliances <= 1000:
    warranty_of_appliance = cost_appliances * 0.5
else:
    warranty_of_appliance = cost_appliances * 0.10

total_cost = cost_appliances + warranty_of_appliance

#output
print (f"Appliances: {name_appliances}")
print (f"Cost of appliances: ${cost_appliances:,.2f}")
print (f"Cost od warranty: ${warranty_of_appliance:,.2f}")
print (f"Total cost: ${total_cost:,.2f}")
