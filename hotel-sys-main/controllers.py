from services import CustomerService

customer_service = CustomerService()

class CustomerController:
    def check_in_customer_handler(self):
        print("To check in a new customer, kindly answer the following questions.")
        first_name = input("What is your first name?: ")
        last_name = input("What is your last name?: ")
        gender = input("What is your gender?: ")
        days = input("What is the length of stay?: ")

        return customer_service.check_in_customer(first_name, last_name, gender, days)

    def check_out_customer_handler(self):
        print("To check out a customer, kindly answer the following questions")
        id = input("What is the customer's ID?: ")

        return customer_service.check_out_customer(id)

    def search_for_customer_by_surname(self):
        print("To search for a customer, kindly provide the following data")
        last_name = input("What is the customer's last name?: ")

        return customer_service.search_for_customer(last_name)

    def delete_customer(self):
        print("To delete a customer record, kindly provide the following details.")
        id = input("What is the customer's ID?: ")

        return customer_service.delete_customer(id)

    def list_all_customer(self):
        print("Listing all Customer Records")

        return customer_service.list_all_customers()

    def get_sys_summary(self):
        print("Getting System Summary")

        return customer_service.print_summary()