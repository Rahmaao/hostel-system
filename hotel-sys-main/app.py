from controllers import CustomerController

customer_controller = CustomerController()


while True:
    resp = input(
        """
Welcome to the Hotel System.
Below is a list of operations you can perform:
1. Check in a Customer.
2. Check out a Customer.
3. Search for a Customer by Surname.
4. Delete a Customer Record.
5. List all Customers in the Database.
6. Print Summary of System.
0. Quit

        """
    )

    if resp == '0':
        print('Goodbye')
        break
    elif resp == '1':
        # print('Checking in a customer')
        customer_controller.check_in_customer_handler()
    elif resp == '2':
        # print('Checking out a customer')
        customer_controller.check_out_customer_handler()
    elif resp == '3':
        # print('Searching for a customer by surname')
        customer_controller.search_for_customer_by_surname()
    elif resp == '4':
        # print('Deleting a Customer Record')
        customer_controller.delete_customer()
    elif resp == '5':
        # print('Listing all customers')
        customer_controller.list_all_customer()
    elif resp == '6':
        # print('Printing System Summary')
        customer_controller.get_sys_summary()
    else:
        print('Invalid Input')