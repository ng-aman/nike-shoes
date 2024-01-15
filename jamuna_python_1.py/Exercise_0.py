# Product details
p1name, p1price = "Laptop", 1200.0
p2name, p2price = "Headphones", 50.0
p3name, p3price = "Mouse", 20.0

# Shopping cart
Shopping_cart= []

# Add items to the cart
Shopping_cart.append({"name": p1name, "price": p1price, "quantity": 2})
Shopping_cart.append({"name": p2name, "price": p2price, "quantity": 1})
Shopping_cart.append({"name": p3name, "price": p3price, "quantity": 3})

# Calculate total amount
total_amt = sum(i["price"] * i["quantity"] for i in Shopping_cart)

# Apply a discount of 10% for a purchase above $100
discount= 0.0
if total_amt > 100:
    discount= 0.1 * total_amt

# Calculate the final amount after applying the discount
final_amt = total_amt - discount

# Display the receipt
print("------ Shopping Receipt ------")
for i in Shopping_cart:
    print(f"{i['name']} x {i['quantity']}: ${i['price'] * i['quantity']}")

print(f"\nTotal Amount: ${total_amt}")
print(f"Discount (10% for purchases above $100): ${discount}")
print(f"Final Amount: ${final_amt}")
