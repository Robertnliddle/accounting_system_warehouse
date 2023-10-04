"""
1. Display all the commands upon launch
2. Each command should display and have their own unique thing.
# - 'balance': The program should prompt for an amount to add or subtract from the account.
# - 'sale': The program should prompt for the name of the product, its price, and quantity. Perform necessary
calculations and
update the account and warehouse accordingly.
# - 'purchase': The program should prompt for the name of the product, its price, and quantity. Perform necessary
calculations
and update the account and warehouse accordingly. Ensure that the account balance is not negative after a purchase
operation.
# - 'account': Display the current account balance.
# - 'list': Display the total inventory in the warehouse along with product prices and quantities.
#  - 'warehouse': Prompt for a product name and display its status in the warehouse.
#  - 'review': Prompt for two indices 'from' and 'to', and display all recorded operations within that range. If ‘from’
and ‘to’ are empty, display all recorder operations. Handle cases where 'from' and 'to' values are out of range.
# - 'end': Terminate the program.
3. After executing any command, the program should again display the list of commands and prompt for the next command.

hints:
#- Use a loop to continuously prompt for commands until the 'end' command is entered.
#- Keep track of the account balance and warehouse inventory.
#- Remember to handle edge cases, like invalid command inputs, negative amounts during a 'purchase' operation, or
out-of-range indices during a 'review' operation.
#- The balance, sale, and purchase commands are remembered by the program.
#- Handle user inputs that are not as expected. The program should not crash in these cases, but instead, it should
display an appropriate error message
"""

balance = 0
warehouse = []
history = []

commands_list_msg = """Select a command: 
- balance: add or subtract from the account
- sale: name of product, quantity and update the warehouse accordingly
- purchase: name of the product, its price, quantity and update to warehouse and account
- account: display the current account balance
- warehouse_list: display the total inventory in the warehouse along with products prices and quantities
- warehouse: display a product and its status in the warehouse
- review: Review the history
- end: exit the program"""

commands_add_sub_msg = """Select if you want to add or subtract to the balance
- add 
- subtract"""

while True:
    print(commands_list_msg)
    action = input("Select a command: ")
    print("Selected command: ", action)
    if action == "end":
        print("Exiting the program...")
        break

    elif action == "balance":
        commands_add_sub_msg = input("Select if you want to add or subtract to the balance: ")
        print(commands_add_sub_msg)
        if action == "add":
            amount = int(input("Enter the amount to add to the balance: "))
            balance += amount
            print("The amount have been added to the balance")
        elif action == "subtract":
            sub = int(input("Enter the amount to subtract: "))
            balance -= sub
            print("The amount have been subtracted to the balance")
        else:
            print("Invalid number, please try again")
        history.append(balance)

    elif action == "sale":
        product_name = int(input("Enter the products name: "))
        price = input("Enter the price: ")
        quantity = int(input("Enter the quantity sold: "))
        if product_name in warehouse:
            total_price = price * quantity
            balance += total_price
            print(f"Products sold:{product_name},Quantity:{quantity}")
        else:
            print("Product not found in the warehouse or the quantity is not enough")
        history.append(f"{product_name} is out of order")

    elif action == "purchase":
        purchase = input("Enter the name of the product: ")
        price = input("Enter the price: ")
        quantity = int(input("Enter the quantity: "))
        total_price = price * quantity
        print(f"You purchase {purchase}{quantity} items for {total_price}")
        if product_name in warehouse:
            history[product_name][quantity] += 1

        if product_name not in warehouse:
            history[product_name][quantity] += 1
        else:
            # total_price > balance ? 
            print("You have to low balance in your account")
            history.append(purchase)

    elif action == "account":
        print(f"Current account balance is: {balance} ")

    elif action == "warehouse_list":
        for product_name, quantity in history():
            print(f"{product_name}: {quantity}")

    elif action == "warehouse":
        warehouse_product = input("Enter the products name: ")
        if product_name in warehouse[product_name][quantity] > 0:
            print(f"{product_name}: {quantity} available at {price} each")
        else:
            print(f"The product name you are looking for are not in the warehouse")
        history.append(product_name)

    elif action == "review":
        from_idx = input("Enter the start of the indices: ")
        to_idx = input("Enter the second value of the indices: ")

    else:
        print(f"The command are not supported {action}. Please select another command.")
