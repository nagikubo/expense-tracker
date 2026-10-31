# expense-tracker + installment 4, Author: Francis Kim G. Canoza

print("=" * 40)
print("\t   EXPENSE TRACKER")
print("  Are you ready to track your expenses?")
print("=" * 40)
print("MAIN MENU")
print("  [1] Add an expense\t\t(coming soon)")
print("  [2] View all expenses\t(coming soon)")
print("  [3] Show total spent\t(coming soon)")
print("  [4] Exit\t(coming soon)\n")

name = input("What's your name? ")
print(f"Welcome, {name}! Let's log two expenses.\n")

def get_message(amount1, amount2=None, is_combo_check=False):
    if is_combo_check:
        if amount1 > 100 and amount2 > 100:
            return "Two big expenses in a row - slow down!"
        return None
    if amount1 > 200:
        return "Huge Expense - are you sure?"
    elif amount1 > 100:
        return "Big Expense."
    elif amount1 > 50:
        return "Moderate Expense."
    else:
        return "Small Expense."

item1 = input("First expense? ")
amount1 = float(input("Amount? "))
msg1 = get_message(amount1)
print(f"  {msg1}")
item2 = input("Second expense? ")
amount2 = float(input("Amount? "))

combo_msg = get_message(amount1, amount2, is_combo_check=True)
if combo_msg:
    msg2 = combo_msg
else:
    msg2 = get_message(amount2)
print(f"  {msg2}")

tax_percent = float(input("Tax rate %? "))
budget = float(input("Your budget? "))
subtotal = amount1 + amount2
average = subtotal / 2
tax = subtotal * (tax_percent / 100)
total = subtotal + tax
over_budget = total > budget
left = budget - total

if over_budget:
    over_amount = total - budget
    verdict = f"Over budget by ${over_amount:.1f}!"
elif total > (budget * 0.90):
    verdict = f"Careful: only ${left:.1f} left."
else:
    verdict = f"Within budget. ${left:.1f} left."

print("-" * 40)
print("SUMMARY")
print(f"  - {item1}:\t\t${amount1:.1f}")
print(f"  - {item2}:\t\t${amount2:.1f}")
print(f"Subtotal:\t\t${subtotal:.1f}")
print(f"Average:\t\t${average:.1f}")
print(f"Tax ({tax_percent:.1f}%):\t\t${tax:.1f}")
print(f"Grand total:\t\t${total:.1f}")
print(f"{verdict}")
print("-" * 40)
print("Made by: Francis Kim G. Canoza  |  Installment 4")