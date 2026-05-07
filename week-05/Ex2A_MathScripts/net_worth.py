# Assets are property and bank account
# Loans are credit card and student 

# Display total debt,assets and net worth

student_loan = 250000
credit_card = 2000
bank_account = 400000
house = 500000

#calculate total assets
total_assets = bank_account + house

#calculate total loans
total_loans = credit_card + student_loan

#calculate total net worth
net_worth = total_assets - total_loans

#printing total assets,loans, and net worth
print('Your total assets are',total_assets)
print('Your total debts are',total_loans)
print('Your net worth is',net_worth)