
#Exercise 3.A - Rewards Program (optional)

cust_list = [] 

class RewardsProgram:
    """Stores basic customer info for a restaurant rewards program."""
    
    def __init__(self, cust_name, phone, email):
        self.cust_name = cust_name
        self.phone = phone
        self.email = email


    def profile(self):
        print(f"Name:  {self.cust_name}")
        print(f"Phone: {self.phone}")
        print(f"Email: {self.email}")

    def thank_you(self):
        print(f"Thank you, {self.cust_name}, for visiting our restaurant!")

    def add_to_cust_list(self):
        cust_list.append((self.cust_name, self.phone, self.email))


c1 = RewardsProgram("Alex Rivera", "555-111-2222", "alex@example.com")
c2 = RewardsProgram("Jordan Lee", "555-333-4444", "jordan@example.com")
c3 = RewardsProgram("Sam Patel", "555-555-6666", "sam@example.com")
for c in (c1, c2, c3):
    c.profile()
    c.thank_you()
c.add_to_cust_list()


print("\nCustomer list:")
print(cust_list)