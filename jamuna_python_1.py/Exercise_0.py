# Product details
p1name, p1price = "Laptop", 1200.0
p2name, p2price = "Headphones", 50.0
p3name, p3price = "Mouse", 20.0

# Shopping cart
c = []

# Add items to the cart
c.append({"name": p1name, "price": p1price, "quantity": 2})
c.append({"name": p2name, "price": p2price, "quantity": 1})
c.append({"name": p3name, "price": p3price, "quantity": 3})

# Calculate total amount
ta = sum(i["price"] * i["quantity"] for i in c)

# Apply a discount of 10% for a purchase above $100
d = 0.0
if ta > 100:
    d = 0.1 * ta

# Calculate the final amount after applying the discount
fa = ta - d

# Display the receipt
print("------ Shopping Receipt ------")
for i in c:
    print(f"{i['name']} x {i['quantity']}: ${i['price'] * i['quantity']}")

print(f"\nTotal Amount: ${ta}")
print(f"Discount (10% for purchases above $100): ${d}")
print(f"Final Amount: ${fa}")
