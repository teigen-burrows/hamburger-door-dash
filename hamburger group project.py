# Team 15
# Jake Gillespie, Teigen Burrows, Lily Tait, Zach Tullis, Shandon Lindquist, Ryan Kennedy
# Door Dash Group Project

# Import Random Library
import random

# Create a class for each person that retrieves a person's name 
# and assigns it to a customer (see inheritance relationship from Person to Customer).
class Person():
    def __init__(self):
      self.customer_name = self.randomName()

    # Method that creates a list of faithful customers and then returns the selected customer.
    def randomName(self):
        customer_list = ["Jefe", "El Guapo", "Lucky Day", "Ned Nederlander", \
                       "Dusty Bottoms", "Harry Flugleman", "Carmen", \
                       "Invisible Swordsman", "Singing Bush"]
        customer_index_selection = customer_list[random.randint(0, (len(customer_list)-1))]
        return customer_index_selection
    
# The Customer class inherits from the Person class.
# This class will create an instance variable that is assigned to the Order object.
class Customer(Person):
    def __init__(self):
        super().__init__()
        self.order = Order().randomBurgers()

# This is the Order class that has an aggregate relationship with the Customer. This class has a method contained within it that will
# obtain the number of burgers that each customer/person gets.
class Order():
    def __init__(self):
        self.burger_count = self.randomBurgers()
    
    # This method will generate the number of burgers that a customer will order
    def randomBurgers(self):
        random_burger_count = random.randint(1, 20)
        return random_burger_count

# Main Program
# Create the queue and initialize the dictionary
lstCustomer = []
dictCustomer = {"Jefe": 0, "El Guapo": 0, "Lucky Day": 0, "Ned Nederlander": 0, \
                       "Dusty Bottoms": 0, "Harry Flugleman": 0, "Carmen": 0, \
                       "Invisible Swordsman": 0, "Singing Bush": 0}

# For loop that will create each customer object, the queue, and the dictionary
for iCount in range(0, 100):
  # Create the Customer Object
  oCustomer = Customer()
  # Create the Queue
  lstCustomer.append([oCustomer.customer_name, oCustomer.order])
  # Create the Dictionary
  dictCustomer[oCustomer.customer_name] += oCustomer.order
  # Pop off of the queue
  lstCustomer.pop(0)
    
# Sort the customers based on their total burgers consumed
lstSortedCustomers = sorted(dictCustomer.items(), key=lambda x: x[1], reverse=True)

# Print out the Ordered Customer List that is formatted
for Customer, random_burger_count in lstSortedCustomers:
  print(Customer.ljust(25) + str(random_burger_count))
