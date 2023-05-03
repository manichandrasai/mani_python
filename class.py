# resturant management system
class Restaurant:
    def __init__(self, name, location, city):
        self.name = name
        self.location = location
        self.city = city
        self.menu = []
        self.orders = {}
        self.tables = {}

    def add_menu_item(self, name, price):
        self.menu.append({"name": name, "price": price})

    def display_menu(self):
        print(" *** Welcome to CAFE COFFE DAY ,HERE IS THE MENU *** ")
        for item in self.menu:
            print(f" {item['name']} - RS {item['price']}")

    def add_order(self, table_number, order_items):
        if table_number in self.orders:
            self.orders[table_number].extend(order_items)
        else:
            self.orders[table_number] = order_items

    def display_orders(self):
        print("Orders:")
        for table_number, order_items in self.orders.items():
            print(f"Table {table_number}: {order_items}")

    def add_table(self, table_number, capacity):
        self.tables[table_number] = capacity

    def display_tables(self):
        print("Tables:")
        for table_number, capacity in self.tables.items():
            print(f"Table {table_number}: Capacity {capacity}")

# Example usage
restaurant = Restaurant("CAFE COFFEE DAY", "Jubilee Hills", "Hyderabad")
print("Restaurant Name:", restaurant.name)
print("Location:", restaurant.location)
print("City:", restaurant.city)

# Add menu items
restaurant.add_menu_item("Paneer Burger", 120)
restaurant.add_menu_item("Veg Pizza", 250)
restaurant.add_menu_item("Salad", 90)
restaurant.add_menu_item("Grill chicken Sandwich", 170)
restaurant.add_menu_item("Chicken Pizza", 320)
restaurant.add_menu_item("ChickenSalad", 130)
restaurant.add_menu_item("Chicken Burger", 120)
restaurant.add_menu_item("Hot Grill Chicken Pizza", 400)
restaurant.add_menu_item("Mushroom Salad", 90)
restaurant.add_menu_item("Cappuccino", 180)
restaurant.add_menu_item("Black Coffee", 150)
restaurant.add_menu_item(" Latte/Iced Latte", 170)
restaurant.add_menu_item("Americano", 160)
restaurant.add_menu_item("Mocha", 150)
restaurant.add_menu_item("Cold coffee", 350)
restaurant.add_menu_item("Hot chcoloate", 220)
restaurant.add_menu_item("Red Velvet Cake.", 180)
restaurant.add_menu_item("Coffee Cake", 150)
restaurant.add_menu_item("Cheesecake", 170)

# Display menu
restaurant.display_menu()

# Add tables
restaurant.add_table(1, 3)
restaurant.add_table(2, 4)
restaurant.add_table(3, 2)
# Display tables
restaurant.display_tables()

# Take orders
restaurant.add_order(1, ["Grill chicken Sandwich","Mushroom Salad", "Hot chcoloate"])
restaurant.add_order(2, ["Red Velvet Cake", "Cappuccino", "Veg Pizza","Cheese cake"])
restaurant.add_order(3, ["Chicken Pizza","Americano"])

# Display orders
restaurant.display_orders()
