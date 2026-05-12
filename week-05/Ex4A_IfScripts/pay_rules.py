pay_rate = float(input('What is your hourly pay: '))
hours_worked = float(input('How many hours did you work: '))
overtime = float(input('Did you work overtime(if yes how many hours): '))


overtime_calc = (pay_rate * 1.5) * overtime
gross_pay = pay_rate * hours_worked + overtime_calc

print(f"""
Pay Rate    Hours Worked    Overtime    Gross Pay
${format(pay_rate,".2f")}             {hours_worked}          {overtime}      ${format(gross_pay,".2f")}
""")
