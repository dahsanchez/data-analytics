sales_data = [
 ('Marcus Webb', 'East', 4250.00),
 ('Priya Sharma', 'West', 5875.50),
('DeShawn Carter', 'East', 3100.75),
 ('LaTonya Rivers', 'South', 6420.00),
 ('Bob Nguyen', 'West', 4980.25),
]
for name, regoin, sales in sales_data:
    if sales > 5000:
        print(f'{name}({regoin}) ${format(sales,".2f")} <--- Top Preformer')
    else:
        print(f'{name}({regoin}) ${format(sales,".2f")}')
