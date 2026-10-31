# expense-tracker + installment 5, Author: Francis Kim G. Canoza

print("=" * 40)
print("\t   EXPENSE TRACKER")
print("  Are you ready to track your expenses?")
print("=" * 40)

name = input("What's your name? ")
tax_percent = float(input("Tax rate %? "))
budget = float(input("Your budget? "))
print(f"Welcome, {name}!\n")

subtotal = 0.0
count = 0

while True:
    print("\nMAIN MENU")
    print("  [1] Add an expense")
    print("  [2] View all expenses (coming soon)")
    print("  [3] Show total spent")
    print("  [4] Exit\n")
    choice = input("Choose 1-4: ")
    
    if choice == "1":
        amount = float(input("Amount? "))
        subtotal += amount
        count += 1
        if amount > 200:
            print("  Huge Expense - are you sure?")
        elif amount > 100:
            print("  Big Expense.")
        elif amount > 50:
            print("  Moderate Expense.")
        else:
            print("  Small Expense.")
            
    elif choice == "2":
        print("  Coming soon: the tracker can't remember each item yet.")
    elif choice == "3":
        tax = subtotal * (tax_percent / 100)
        total = subtotal + tax
        left = budget - total
        if total > budget:
            over_amount = total - budget
            verdict = f"Over budget by ${over_amount:.1f}!"
        elif total > (budget * 0.90):
            verdict = f"Careful: only ${left:.1f} left."
        else:
            verdict = f"Within budget. ${left:.1f} left."
        print(f"  Expenses:\t{count}")
        print(f"  Subtotal:\t${subtotal:.1f}")
        print(f"  Tax ({tax_percent:.1f}%):\t${tax:.1f}")
        print(f"  Grand total:\t${total:.1f}")
        print(f"  {verdict}")
    elif choice == "4":
        print(f"Goodbye, {name}!")
        print("-" * 40)
        print("Made by: Francis Kim G. Canoza  |  Installment 5")
        print("-" * 40)
        break
    else:
        print("  Please choose 1, 2, 3 or 4.")