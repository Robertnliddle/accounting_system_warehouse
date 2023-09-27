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
amount = []
product_name = []
account = []
balance = []
sale = []

purchase = 0
warehouse = 0
review = 0

commands_list_msg = """Select a command: 
- balance: add or subtract from the account
- sale: name of product, quantity and update the warehouse accordingly
- purchase: name of the product, its price, quantity and update to warehouse and account
- account: display the current account balance
- warehouse_list: display the total inventory in the warehouse along with products prices and quantities
- warehouse: display a product and its status in the warehouse
- review: Prompt for two indices 'from' and 'to', and display all recorded operations within that range
- end: exit the program"""

while True:
    print(commands_list_msg)
    action = input("Select a command: ")
    print("Selected command: ", action)
    if action == "end":
        print("Exiting the program...")
        break

    elif action == "balance":
        amount = int(input("Enter the amount to add/subtract to the account: "))
        print("The amount have been added to the account")
        if amount == 0:
            print("Invalid number, please try again")
        balance += amount
        new_money = {"balance": amount}
        balance.append(amount)

    elif action == "sale":
        product_name = int(input("Enter the products name: "))
        price = input("Enter the price: ")
        quantity = int(input("Enter the quantity: "))
        print("Updated the sales")
        warehouse = product_name
        sale.append(sale)

    elif action == "purchase":
        purchase = int(input("Enter the name of the product: "))
        price = int(input("Enter the price: "))
        quantity = int(input("Enter the quantity: "))
        print(f"You purchase {purchase}{quantity} items")
        sale.append(purchase)

    elif action == "account":
        print(f"Current account balance is: {balance} ")
        account.append(balance)

    elif action == "warehouse_list":
        print(f"List of all the products in the warehouse {product_name}: {quantity} at {price}")
        sale.append(product_name)

    elif action == "warehouse":
        warehouse_product = input("Enter the products name: ")
        if product_name:
            print(f"{product_name}: {quantity} available at {price} each")
        else:
            print(f"{product_name} is not in the warehouse")
        product_name =
        sale.append(product_name)

    elif action == "review":
        first_indices = int(input("Enter the first value of the indices: "))
        second_indices = int(input("Enter the second value of the indices: "))

        if first_indices or second_indices == 0:
            print("Invalid value, please try again.")

    else:
        print(f"The command are not supported {action}. Please select another command.")
