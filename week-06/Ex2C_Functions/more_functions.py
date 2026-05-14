def display_mailing_label(name,address,city,state,zip):
    return(f'''{name}
{address}
{city}{state}{zip} ''')


def add_numbers(*result):
    total = sum(result)
    numbers_string = " + ".join(str(num) for num in result)
    print(f"{numbers_string} = {total}")

def display_receipt(total_due, amount_paid):
    print(f"Total Due: ${total_due}")
    print(f"Amount Paid: ${amount_paid}")
    
    if amount_paid >= total_due:
        change = amount_paid - total_due
        print(f"Change Due: ${change}")
    else:
        balance = total_due - amount_paid
        print(f"Remaining Balance: ${balance}")

print(display_mailing_label(
    'Dahlia',
    '1140 D St Apt 109',
    'Hayward',
    'CA',
    '94541'
    ))

print(display_mailing_label(
    "John Smith",
    "456 Oak Avenue",
    "Los Angeles",
    "CA",
    "90001"
))

print(add_numbers(1))
print(add_numbers(1,4,6))
print(add_numbers(18,20,300))

print(display_receipt(30,55))
print(display_receipt(40,40))
print(display_receipt(60,30))