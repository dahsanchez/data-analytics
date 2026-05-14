def display_mailing_label(name,address,city,state,zip):
    return(f'''{name}
{address}
{city}{state}{zip} ''')


def add_numbers(*result):
    total = sum(result)
    numbers_string = " + ".join(str(num) for num in result)
    print(f"{numbers_string} = {total}")
