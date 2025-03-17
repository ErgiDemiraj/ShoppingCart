         +-------------+
         |  Product    |
         +-------------+
              ^
              |
     +------------------+
     |    DigitalProduct |
     +------------------+       +-------------------+
              |                |   PhysicalProduct  |
              +---------------->+-------------------+
                          |
                    +------------------+
                    |      Cart         |
                    +------------------+
                          |
                     +--------+
                     |  User  |
                     +--------+
                          |
              +-------------------------+
              |     Discount (Abstract) |
              +-------------------------+
                     |            |
        +----------------+   +-------------------+
        | Percentage     |   | FixedAmount       |
        | Discount       |   | Discount          |
        +----------------+   +-------------------+
1. The product class has the attributes of the products, can update the quantity and retrieve the poduct information.
2. The DigitalProduct class is inherited from the Product class so that it can include digital products as well, and it has some extra attributes.
3. The PhysicalProduct class is inherited from the Product class so that it can include physical products and also has some extra attributes that differ from the digital product.
4. The cart clas creates a private list of cart items to store the products and they are different from each user.
5. The User Class has the user which will have the cart.
6. The Discount class is an abstract class which has the method for the discount.
7 & 8 Then either the Percentage discount or the fixed discoun will be chosen which will apply the discoun based on a percentage of the total amoun or a fixed amount. 