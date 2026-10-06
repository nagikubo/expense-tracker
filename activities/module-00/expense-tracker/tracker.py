# expense-tracker + installment 3, Author: Francis Kim G. Canoza, program for tracking expenses, someone's appetite and more.

print("=" * 40)
print("\t   EXPENSE TRACKER")
print("  Are you ready to track your expenses?")
print("=" * 40)
print("Main Menu")
print("[1] Add Expense\t\t(coming soon)")
print("[2] View all expenses\t(coming soon)")
print("[3] Show total spent\t(coming soon)")
print("[4] Exit program\t(coming soon)")

name = input("\nWhat's your name? ")
print(f"Welcome, {name}! Let's log two expenses.\n")

subtotal = 0

item1 = input("First expense? ")
amount1 = float(input("Amount? "))
item2 = input("Second expense? ")
amount2 = float(input("Amount? "))
tax_percent = float(input("Tax rate in whole numbers %? "))
budget = float(input("Total budget? "))

subtotal = amount1 + amount2
average = subtotal / 2
tax = subtotal * (tax_percent / 100)
total = subtotal + tax
over_budget = total > budget
left = budget - total

print(f"-" * 40) 
print("Summary")
print(f"  -{item1}:\t\t${amount1}")
print(f"  -{item2}:\t\t${amount2}")
print(f"Subtotal:\t\t${subtotal}")
print(f"Average:\t\t${average}")
print(f"Tax ({tax_percent}%):\t\t${tax}")
print(f"Grand Total Spent:\t${total}")
print(f"Over budget?\t\t{over_budget}")
print(f"Left in budget:\t\t${left}")
print("-" * 40) 

print("Made by Francis Kim G. Canoza | Installment 3")
