# Step 1: Create Products
digital_product = DigitalProduct(
    product_id=101,
    name="E-book",
    price=10.00,
    quantity=5,
    file_size=2,
    download_link="http://example.com/download/ebook"
)

physical_product = PhysicalProduct(
    product_id=102,
    name="Laptop",
    price=1000.00,
    quantity=3,
    weight=2.5,
    dimensions="35x25x3 cm",
    shipping_cost=20.00
)

# Step 2: Create a User
user = User(user_id=1, name="John Doe")

# Step 3: Add Products to Cart
user.add_to_cart(digital_product)
user.add_to_cart(physical_product)

# Step 4: View Cart
print("Current Cart:")
print(user.cart.view_cart())

# Step 5: Apply Discount
percentage_discount = PercentageDiscount(percentage=10)
total_after_percentage_discount = user.cart.apply_discount(percentage_discount)
print(f"\nTotal after 10% discount: ${total_after_percentage_discount}")

# Step 6: Apply Fixed Discount
fixed_discount = FixedAmountDiscount(amount=50)
total_after_fixed_discount = user.cart.apply_discount(fixed_discount)
print(f"\nTotal after $50 discount: ${total_after_fixed_discount}")

# Step 7: Checkout
print("\nCheckout:")
print(user.checkout())
