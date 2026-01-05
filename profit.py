actual_amount = float(input("Please enter your actual amount: ₹ "))
selling_amount = float(input("Please Enter your selling amount: ₹ "))

if (selling_amount > actual_amount):
    profit = selling_amount - actual_amount
    print(f"You have profit of {profit}")
else:
    loss = actual_amount - selling_amount
    print(f"You have no profit, this is your loss {loss}")