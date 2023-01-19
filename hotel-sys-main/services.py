from database import Session, Customer

session = Session()

class CustomerService:
    def check_in_customer(self, first_name: str, last_name: str, gender:  str, days: int ):
        print(f"Checking in Customer: {first_name} {last_name}")
        customer = Customer(
            first_name = first_name,
            last_name = last_name,
            gender = gender,
            days = days,
        )
        
        session.add(customer)
        session.commit()

    def check_out_customer(self, id: str):
        print(f"Checking out customer with id {id}")
        customer = session.query(Customer).get(id)

        if not customer:
            print(f"There is no such Customer with the ID {id}")
        else:
            customer.checked_in = False
            session.commit()
            print("Customer has been Checked out succesfully")

    def search_for_customer(self, last_name: str):
        print(f"Searching for Customer with Surname {last_name}")
        customers = session.query(Customer).filter_by(last_name=last_name)
        [print(f"{customer.serialize_me()}\n") for customer in customers]

    def delete_customer(self, id: str):
        print(f"Deleting Customer with ID {id}")
        customer = session.query(Customer).get(id)

        if not customer:
            print(f"There is no such customer with that ID {id}")
        # elif customer.checked_in == True:
        #     print(f"This customer with ID {id} has already checked in. The reservation cannot be deleted")
        else:
            session.delete(customer)
            session.commit()

    def list_all_customers(self):
        print(f"Listing all Customers in System")
        customers = session.query(Customer).all()
        [print(f"{customer.serialize_me()}\n") for customer in customers]

    def print_summary(self):
        print(f"Listing all Customers in System")
        all_customers = session.query(Customer).count()
        checked_in = session.query(Customer).filter_by(checked_in = True).count()
        checked_out = all_customers - checked_in
        print(
            f"System Summary: \n Total Records: {all_customers} \n Checked In: {checked_in} \n Checked Out {checked_out}"
        )
