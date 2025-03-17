class Product:
    def __init__(self,product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity
        #Created the product class and added the attributes.
        
    def update_quantity(self, new_quantity):
        self.quantity = new_quantity
    
    def get_product_info(self):
        return f"ID: {self.product_id}, Name: {self.name}, Price:${self.price}, Quantity: {self.quantity}"
    #I added the methods
    #Step 1 done
    #Step 1 findings and thoughts: There was nothing to think about when creating the class
    # and adding the attributes. When you update the quantity, you must not forget to assign
    # it to the self.quantity. 
    #Step 2
class DigitalProduct(Product):
    def __init__ (self, product_id, name, price, quantity, file_size, download_link):
        super().__init__ (product_id, name, price, quantity)
        self.file_size = file_size
        self.download_link = download_link
    #I added the aditional attributes.
    #Findings and thoughts: The super().__init__ comand is very important here
    # because if I did not add that then the Digital Product class would not have
    # access to the attributes of the parent class and would result in an error.
    def get_product_info(self):
        return (f"ID: {self.product_id}, Name:{self.name}, Price: ${self.price},"
                f"Quantity: {self.quantity}, File Size:{self.file_size}MB, "
                f"Download Link:{self.download_link}")
    #Step 2 done
    #Step 3
class PhysicalProduct(Product):
    def __init__ (self, product_id, name, price, quantity,weight, dimensions, shipping_cost ):
        super().__init__ (product_id, name, price, quantity)
        self.weight = weight
        self.dimensions = dimensions
        self.shipping_cost = shipping_cost
    #Same procces as step 2
    def get_product_info(self):
        return (f"ID: {self.product_id}, Name:{self.name}, Price: ${self.price},"
                f"Quantity: {self.quantity}, Weight: {self.weight}lb, "
                f"Dimensions: {self.dimensions}, Shipping Cost: ${self.shipping_cost}")
    #Step 3 was the same as step 2, just different attributes.
    #Step 4
class Cart:
    def __init__ (self):
        self.__cart_items = []
    #a list to store products
    #Used __ before cart_items to keep it private
    def add_product(self, product):
        self.__cart_items.append(product)
    #used append to add the product to the list
    def remove_product(self, product_id):
        for product in self.__cart_items:
            if product.product_id == product_id:
                self.__cart_items.remove(product)
                break 
    #used .remove to remove the product.
    # break is important because there can be errors if not used. but it only removes 1 product.
    def view_cart(self):
        if not self.__cart_items:
            return "Cart is empty"
        cart_info = ""
        for product in self.__cart_items:
            cart_info += product.get_product_info()
        return cart_info
    #If the cart is empty you get a message saying its empty.
    #cart_info is empty but it collects products with the product.get_product_info()
    def calculate_total(self):
        return sum(product.price for product in self.__cart_items)
    # get the price of the product with product.price for each product in cart_items.
    # and the sum adds all of the prices.
    def apply_discount(self, discount):
        total = self.calculate_total()
        return discount.apply_discount(total)
    # applied polymorphism in here so that the command can be applied to either the fixed discount or the percentage discount
    #Step 5
class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.cart = Cart()
        # added the attributes and created an instance of the Cart class
        # a Cart will be created for each User. The Cart() will start with an empty cart
        # Each user will have their own cart
    def add_to_cart(self,product):
        self.cart.add_product(product)
        # takes the user's cart and adds a product to it.
        #The cart was once empty but it gets filled with products
        # add_product adds the given product "(product)" to the list of the cart
    def remove_from_cart(self, product_id):
        self.cart.remove_product(product_id)
        # It removes a product based on the product_id that is given.
        #There will only be removed one product at a time with that id
    def checkout(self):
        total = self.cart.calculate_total()
        self.cart = Cart()
        return f"Total amount: ${total}. Cart is now empty"
    # it uses the calculate_total command from the cart class.
    #It sums the price of all items in the user's cart and calculates the total.
    # After getting the total I emptied the cart by using self.cart = Cart()
    # step 6
if __name__ == "__main__":
    
    product1 = Product(1, "Laptop", 1000, 5)
    product2 = Product(2, "Phone", 500, 3)

    
    user = User(1, "John Doe")

    
    user.add_to_cart(product1)  
    user.add_to_cart(product2)  
    print("User's Cart after adding products:")
    print(user.cart.view_cart())  

    
    user.remove_from_cart(1) 
    print("\nUser's Cart after removing Laptop:")
    print(user.cart.view_cart())  

    
    print("\nCheckout process:")
    total_before_checkout = user.cart.calculate_total()
    print(f"Total before checkout: ${total_before_checkout}")
    checkout_message = user.checkout()  
    print(checkout_message)
    
    try:
        print(user.cart.__cart_items) 
    except AttributeError as e:
        print("\nError: Cannot access __cart_items directly:", e)
# from abc import ABC, abstractmethod
# #abc abstrace basic class
# #Define an abstract class (Page82 slide 6)
# class Discount(ABC):
#     @abstractmethod
#     def apply_discount(self, total_amount):
#         pass
#     # Step 7
# class PercentageDiscount(Discount):
#     def __init__ (self, percentage):
#         self.percentage = percentage
#         #attribute percentage
#     def apply_discount(self, total_amount):
#         discount = total_amount * (self.percentage / 100)
#         return total_amount - discount
#     #It gets a percentage then it multiplies that with the total to get the discount
#     # in the end it returns the difference between the total abount and the discount
#     # which is the final price.
#     # Step 8
# class FixedAmountDiscount(Discount):
#     def __init__(self, amount):
#         self.amount = amount
#     def apply_discount(self, total_amount):
#         return total_amount - self.amount
#     # the self.amount gives a fix discount which isn't based on a percentage
#     # and when you apply that discount, it takes the difference between the total
#     # amount and the discount amount to give the final amount. 
#         
        