# calc pay based of hours worked at $18/hr

rate_p_h = 18 # rate per hour
tax_rate = 0.30 # tax rate of 30%

print("your hourly rate is $18/hr.\nenter your hours worked to calculate pay")
print("------------")
hours_worked = float(input("hours worked: "))

print("------------")
print("based off the amount of hours you worked (" + str(hours_worked) + "), your pay is $" + str(18*hours_worked))
print("------------")
print("oh no! you must pay tax")
print("after tax (" + str(tax_rate*100) + "%), your pay is $" + str((18*hours_worked)*(1-tax_rate)))
