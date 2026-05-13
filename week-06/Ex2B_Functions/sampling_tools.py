import random

products = ['Laptop', 
            'Monitor', 
            'Keyboard', 
            'Mouse', 
            'Webcam', 
            'Headset', 
            'Docking Station', 
            'USB Hub', 
            'Desk Lamp', 
            'Surge Protector'
            ]   

product_of_day = random.choice(products)
print(f"Today's product of the day is: {product_of_day}")

survey = random.sample(products,3)
print(f"Today's survey products are: {survey}")

shuffle_products = random.shuffle(products)
print(f"Shuffled products: {products}")

daily_transaction = random.randint(50, 300)
print(f"Today's total transactions: {daily_transaction}")