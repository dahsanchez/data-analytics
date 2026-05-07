# Assets are property and bank account
# Loans are credit card and student 

# Display total debt,assets and net worth

student_loan = 250000
credit_card = 2000
bank_account = 400000
house = 500000

total_assets = bank_account + house
total_loans = credit_card + student_loan
net_worth = total_assets - total_loans

print('Your total assets are',total_assets)
print('Your total debts are',total_loans)
print('Your net worth is',net_worth)