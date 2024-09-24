ACTION_PROMPT = "Enter (1) to add an expense | (2) to view expenses | (3) to delete an expense | or (4) to reset your expenses: "
DEL_CATEGORY_PROMPT = "Enter the Category you want to delete from: "


def greeting():
        print("""Welcome to Expense Tracker! Expense Tracker is designed to keep track of all your expenses.
You can add expenses, delete expenses, view expenses, and clear all your expenses!\n""")


expenses = {}


def select_action():
        action = input(ACTION_PROMPT)
        while action not in ["1", "2", "3", "4"]:
            print("Invalid input")
            action = input(ACTION_PROMPT)
        return action


def adding_expense():
        while True:
            category = input("Enter the category of the expense (e.g, food, transportation, entertainment, E.T.C): ").capitalize().strip()

            while True:
                try: 
                    value = float(input("Enter the expense value: "))
                    break
                except ValueError:
                    print("Invalid input")

            if category not in expenses:
                expenses[category] = [value]
            else:
                expenses[category].append(value)
        
            choice = input("Enter (y) if you would like to add another expense or enter (n) to exit: ").lower()

            if choice != "y":   
                break
            

def show_expenses():
    if not expenses:
         print("Your expense tracker is empty.")
         return

    for category, entries in expenses.items():
        print(f"Category: {category}")
        for value in entries:
            print(f" ${value}")


def delete_expense():
        show_expenses()
        category = input(DEL_CATEGORY_PROMPT)

        while category not in expenses:
            print("Invalid input, category not found")
            category = input(DEL_CATEGORY_PROMPT)

        while True:
            try:
                value = float(input(f"Enter the value you want to delete from {category}: "))
                if value not in expenses[category]:
                     print(f"Invalid input, value not found in {category}")
                else:
                     break
            except ValueError:
                print("Invalid input, please enter a numeric value")
            

        print(f"Deleted {value} from {category}")
        expenses[category].remove(value)
        if not expenses[category]:
            del expenses[category]
            print(f"Deleted empty category: {category}")


def reset_all_expenses():
        print("All of your expenses have been cleared")
        expenses.clear()


def main(action):
    if action == "1":
        adding_expense()
    elif action == "2":
        show_expenses()
    elif action == "3":
        delete_expense()
    elif action == "4":
        reset_all_expenses()


def summary():
    print("\nThank you for using the expense tracker!")
    if expenses:
        print("Here is a summary of your total expenses per category:\n")
        for category in expenses.keys():
            total = sum(expenses[category])
            print(f"{category} total: ${total}")
    else:
         print("You don't have any expenses!")
    print(f"Your most expensive purchase was ${max(max(expenses.values()))}")
    
    
greeting()

while True:  
    action = select_action() 
    main(action)
    program_control = input("Enter (y) to continue using the expense tracker or (e) to exit the program: ").lower()
    if program_control == "e":
            summary()
            break
