item = input("What item would you like to buy: ")
price = float(input("What is the price?: "))
quantity = int(input("How many would like?: "))
total = price * quantity
print(f"You have bought {quantity} x {item}/2")
print(f"Your total is: ${total}")