from datastructures.array import Array
from datastructures.linkedlist import LinkedList
from datastructures.circularqueue import CircularQueue



class Drink:
    def __init__(self, name, price):
        self.name = name
        self.size = "Medium"
        self.price = price
    pass

class OrderItem:
    def __init__(self, drink, customization=""):
        self.drink = drink
        self.customization = customization
    pass

class CustomerOrder:
    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.items = LinkedList()

    def add_item(self, order_item):
        self.items.append(order_item)

    def __iter__(self):
        return iter(self.items)
    pass

class BistroSystem:
    def __init__(self):
        self.menu = Array(5)
        self.open_orders = CircularQueue(maxsize=100)
        self.completed_orders = LinkedList()
        self._populate_menu()

    def _populate_menu(self):
        self.menu[0] = Drink("Bearcat Mocha", 4.50)
        self.menu[1] = Drink("Campus Cappuccino", 3.75)
        self.menu[2] = Drink("Latte Lift-Off", 4.00)
        self.menu[3] = Drink("Espresso Express", 3.00)
        self.menu[4] = Drink("Study Buddy Brew", 4.25)

    def display_menu(self):
        print("\nBearcat Bistro Menu:")
        for i in range(len(self.menu)):
            drink = self.menu[i]
            if drink:
                print(f"{i + 1}. {drink.name} - ${drink.price:.2f}")

    def take_new_order(self):
        name = input("enter customer name: ")
        order = CustomerOrder(name)

        while True:
            print("/nMenu")
            for i in range(len(self.menu)):
                drink = self.menu[i]
                if drink:
                    print(f"{i + 1}. {drink.name} - ${drink.price:.2f}")
            try:
                choice = int(input("Select a drink number (1-5): ")) - 1
                if choice < 0 or choice >= len(self.menu) or self.menu[choice] is None:
                    print("Invalid Choice")
                    continue
            except ValueError:
                print("Invalic input")
                continue
            customization = input("Any customization? (press enter to skip): ")
            selected_drink = self.menu[choice]
            order_item = OrderItem(selected_drink, customization)
            order.add_item(order_item)
            more = input("Anything Else? (y/n): ").strip().lower()
            if more != 'y':
                break
        print("\nOrderSummary:")
        print(f"Customer: {order.customer_name}")
        for item in order.items:
            print(f"- {item.drink.name} ({item.drink.size}) - ${item.drink.price:.2f}")
            if item.customization:
                print(f"Custom: {item.customization}")
        confirm = input("Confirm order? (y/n): ").strip().lower()
        if confirm == 'y':
            self.open_orders.enqueue(order)
            print("Order added to Queue")
        else:
            print("Order canceled")

    def view_open_orders(self):
        print("\nOpen Orders:")
        if self.open_orders.empty():
            print("No open orders")
            return
        temp_queue = CircularQueue()
        while not self.open_orders.is_empty():
            order = self.open_orders.dequeue()
            print(f"\nCustomer: {order.customer_name}")
            for item in order:
                print(f"- {item.drink.name} ({item.drink.size}) - ${item.drink.price:.2f}")
                if item.customization:
                    print(f"Custom: {item.customization}")
            temp_queue.enqueue(order)
        while not temp_queue.is_empty():
            self.open_orders.enqueue(temp_queue.dequeue())

    def complete_next_order(self):
        if self.open_orders.is_empty():
            print("No orders to complete")
            return
        completed = self.open_orders.dequeue()
        self.completed_orders.append(completed)
        print(f"Completed order for {completed.customer_name}")

    def generate_end_of_day_report(self):
        print("\nEnd-Of-Day Report")
        if self.completed_orders.head is None:
            print("No orders completed today")
            return
        sales_data = {}
        total_revenue = 0
        for order in self.completed_orders:
            for item in order:
                name = item.drink.name
                price = item.drink.price
                if name not in sales_data:
                    sales_data[name] = [0, 0.0]
                sales_data[name][0] += 1
                sales_data[name][1] += price
                total_revenue += price
        for name, data in sales_data.items():
            count, total = data
            print(f"{name}: {count} sold - ${total:.2f}")
        print(f"Total Revenue: ${total_revenue:.2f}")
