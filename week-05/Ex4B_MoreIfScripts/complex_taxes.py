# that will calculate federal tax based on the 
# values of annual gross income (a number) and a filing 
# status (‘single’ or ‘joint’).

pay_rate = float(input('What is your hourly pay: '))
hours_worked = float(input('How many hours did you work: '))
filling = input('Are you filing single or joint: ')

gross_pay = pay_rate * hours_worked
annual_gross_pay = (pay_rate * hours_worked) * 52

if filling == 'single' and annual_gross_pay < 12000:
    tax_withholding = annual_gross_pay * 0.05
    net_pay = annual_gross_pay - tax_withholding
    print(f"""
    You worked {hours_worked} hours this period.
    Because you earn ${format(pay_rate,".2f")} per hour, your gross weekly pay is ${format(gross_pay,".2f")}
    Your filing status is {filling}
    Your tax withholding for the week is ${format(tax_withholding,".2f")}
    Your net pay is ${format(net_pay,".2f")}
    """)
elif filling == 'single' and 12000 <= annual_gross_pay <= 24999.99:
    tax_withholding = annual_gross_pay * 0.1
    net_pay = annual_gross_pay - tax_withholding
    print(f"""
    You worked {hours_worked} hours this period.
    Because you earn ${format(pay_rate,".2f")} per hour, your gross weekly pay is ${format(gross_pay,".2f")}
    Your filing status is {filling}
    Your tax withholding for the week is ${format(tax_withholding,".2f")}
    Your net pay is ${format(net_pay,".2f")}
    """)
elif filling == 'single' and 25000 <= annual_gross_pay <= 74999.99:
    tax_withholding = annual_gross_pay * 0.15
    net_pay = annual_gross_pay - tax_withholding
    print(f"""
    You worked {hours_worked} hours this period.
    Because you earn ${format(pay_rate,".2f")} per hour, your gross weekly pay is ${format(gross_pay,".2f")}
    Your filing status is {filling}
    Your tax withholding for the week is ${format(tax_withholding,".2f")}
    Your net pay is ${format(net_pay,".2f")}
    """)
else:
    tax_withholding = annual_gross_pay * 0.2
    net_pay = annual_gross_pay - tax_withholding
    print(f"""
    You worked {hours_worked} hours this period.
    Because you earn ${format(pay_rate,".2f")} per hour, your gross weekly pay is ${format(gross_pay,".2f")}
    Your filing status is {filling}
    Your tax withholding for the week is ${format(tax_withholding,".2f")}
    Your net pay is ${format(net_pay,".2f")}
    """)

if filling == 'joint' and annual_gross_pay < 12000:
    tax_withholding = annual_gross_pay * 0
    net_pay = annual_gross_pay - tax_withholding
    print(f"""
    You worked {hours_worked} hours this period.
    Because you earn ${format(pay_rate,".2f")} per hour, your gross weekly pay is ${format(gross_pay,".2f")}
    Your filing status is {filling}
    Your tax withholding for the week is ${format(tax_withholding,".2f")}
    Your net pay is ${format(net_pay,".2f")}
    """)
elif filling == 'joint' and 12000 <= annual_gross_pay <= 24999.99:
    tax_withholding = annual_gross_pay * 0.06
    net_pay = annual_gross_pay - tax_withholding
    print(f"""
    You worked {hours_worked} hours this period.
    Because you earn ${format(pay_rate,".2f")} per hour, your gross weekly pay is ${format(gross_pay,".2f")}
    Your filing status is {filling}
    Your tax withholding for the week is ${format(tax_withholding,".2f")}
    Your net pay is ${format(net_pay,".2f")}
    """)
elif filling == 'joint' and 25000 <= annual_gross_pay <= 74999.99:
    tax_withholding = annual_gross_pay * 0.11
    net_pay = annual_gross_pay - tax_withholding
    print(f"""
    You worked {hours_worked} hours this period.
    Because you earn ${format(pay_rate,".2f")} per hour, your gross weekly pay is ${format(gross_pay,".2f")}
    Your filing status is {filling}
    Your tax withholding for the week is ${format(tax_withholding,".2f")}
    Your net pay is ${format(net_pay,".2f")}
    """)
else:
    tax_withholding = annual_gross_pay * 0.2
    net_pay = annual_gross_pay - tax_withholding
    print(f"""
    You worked {hours_worked} hours this period.
    Because you earn ${format(pay_rate,".2f")} per hour, your gross weekly pay is ${format(gross_pay,".2f")}
    Your filing status is {filling}
    Your tax withholding for the week is ${format(tax_withholding,".2f")}
    Your net pay is ${format(net_pay,".2f")}
    """)