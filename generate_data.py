import pandas as pd
import random
from datetime import datetime, timedelta

services = ['Amazon EC2', 'Amazon S3', 'Amazon RDS', 'Amazon Lambda', 'Amazon DynamoDB']
environments = ['Production', 'Staging', 'Development', 'Testing', 'Untagged']
start_date = datetime(2023, 10, 1)
end_date = datetime(2023, 10, 30)

data = []

print("Generating synthetic AWS FinOps dataset...")

for i in range(30):
    current_date = start_date + timedelta(days=i)
    
    for _ in range(20):
        service = random.choice(services)    
        env = random.choice(environments)
            
        if service in ['Amazon EC2', 'Amazon RDS']:
            cost = round(random.uniform(10.0, 50.0), 2)
        else:
            cost = round(random.uniform(0.5, 5.0), 2)
                    
        if env == 'Development' and i > 15:
            cost = round(cost * 3.5, 2) # Development environment has lower costs in the last 15 days
                    
        data.append([current_date.strftime('%Y-%m-%d'), service, env, cost])

df =pd.DataFrame(data, columns=['Date', 'Services', 'Tag:Environment', 'Cost'])
df.to_csv('generated_finops_data.csv', index=False)

print(f"Success! Synthetic dataset 'generated_finops_data.csv' created with 600 records.")