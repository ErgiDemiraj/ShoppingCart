Findings:
Product Class: The Product class was simple, with just attributes for ID, name, price, and quantity. It helped set up the base for other product types.
Super and Inheritance: I learned that super().__init__ is important for child classes to use the attributes and methods from the parent class, like in DigitalProduct and PhysicalProduct.
Removing Products from Cart: I used break in the remove_product method to avoid removing more than one product at once, preventing errors.
Discounts and Polymorphism: I was confused at first about how to apply different discounts, but using polymorphism helped. Now, the cart can handle both percentage and fixed amount discounts.
Abstract Discount Class: Using an abstract class for discounts was helpful to make sure each discount type followed the same structure.

Challenges:
Polymorphism: Understanding how to apply polymorphism to handle multiple discount types was tricky but important for flexibility.
Abstract Classes: I had to learn how to use abstract classes correctly, especially knowing that you can’t instantiate them directly.
Cart Operations: It was a challenge to make sure products were added or removed correctly from the cart.

Limitations and Improvements:
Error Handling: The code doesn't handle errors well, like when trying to remove a product that isn't in the cart.
Discount Checks: There should be checks to ensure discounts aren’t more than the total price.
