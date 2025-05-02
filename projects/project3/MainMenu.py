from projects.project3.Classes import BistroSystem

def main():
    system = BistroSystem()

    while True:
        print("\nWelcome to the Bearcat Bistro!")
        print("1. Display Menu")
        print("2. Take New Order")
        print("3. View Open Orders")
        print("4. Mark Next Order as Complete")
        print("5. View End-of-Day Report")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            system.display_menu()
        elif choice == '2':
            system.take_new_order()
        elif choice == '3':
            system.view_open_orders()
        elif choice == '4':
            system.complete_next_order()
        elif choice == '5':
            system.generate_end_of_day_report()
        elif choice == '6':
            break
        else:
            print("Invalid input. Try again.")

if __name__ == "__main__":
    main()