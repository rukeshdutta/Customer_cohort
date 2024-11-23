import pandas as pd
import numpy as np
from faker import Faker
from datetime import datetime

# Initialize Faker for generating random customer data
faker = Faker()

# Parameters for synthetic data
num_customers = 500
start_date = datetime.strptime('2023-01-01', '%Y-%m-%d').date()
end_date = datetime.strptime('2023-12-31', '%Y-%m-%d').date()
max_orders_per_customer = 10

# Generate synthetic customer data
customers = []
for customer_id in range(1, num_customers + 1):
    # Randomly assign a first purchase date
    first_purchase_date = faker.date_between(start_date=start_date, end_date=end_date)
    num_orders = np.random.randint(1, max_orders_per_customer + 1)
    # Generate multiple purchase dates for the customer
    purchase_dates = [
        faker.date_between(start_date=first_purchase_date, end_date=end_date)
        for _ in range(num_orders)
    ]
    purchase_dates = sorted(purchase_dates)  # Ensure dates are chronological

    for purchase_date in purchase_dates:
        customers.append({
            'customer_id': customer_id,
            'order_date': purchase_date,
            'revenue': round(np.random.uniform(20, 500), 2)  # Random revenue
        })

# Create a DataFrame
df_synthetic = pd.DataFrame(customers)

# Save to CSV (optional)
df_synthetic.to_csv('synthetic_cohort_data.csv', index=False)

# Display first few rows
print(df_synthetic.head())
