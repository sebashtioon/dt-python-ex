# calc pay based of hours worked at $18/hr

print("your hourly rate is $18/hr.\nenter your hours worked to calculate pay")
print("------------")
rate_p_h = 18 # rate per hour
hours_worked = float(input("hours worked: "))
print("------------")
print("based off the amount of hours you worked (" + str(hours_worked) + "), your pay is $" + str(18*hours_worked))

