bank_balance = 1000
saving_goal = 7000
weekly_saving = 300

while bank_balance < saving_goal:
    bank_balance += weekly_saving
    print(f'This week my balance increased to {bank_balance}')
    if bank_balance == 3500:
        print(f'Almost there! This week my balance is up to {bank_balance}.')
    elif bank_balance == 5200:
        bank_balance -= 30
        print(f'So close! After treating myself, my balance is up to {bank_balance}.')
    if bank_balance >= saving_goal:
        print(f'Goal met! My current balance is {bank_balance}')

