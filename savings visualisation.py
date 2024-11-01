import subprocess
import sys

# Check if numpy is installed, if not, install it
try:
    import matplotlib.pyplot as plt
except ImportError:
    print("matplotlib not found. Installing...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "matplotlib"])
    print("matplotlib installed successfully!")

import matplotlib.pyplot as plt

import numpy as np


import pandas as pd


#define our parameters for our modelled savings account
interest_rate = 0.02
rate_of_return = 0.04
weekly_payment = 20
yearly_payment1 = weekly_payment*52
yearly_payment2 = 20000
current_age = 21
first_salary = 22
max_forecast_age = 40
years_forecast = max_forecast_age - current_age
age_array = []
for i in range(current_age, max_forecast_age):
    age_array.append(i)

growth_rate = (1 + rate_of_return)/(1 + interest_rate)

#y0 = 1040
#y1 = 10000  +  1040*(1+j)/(1+i)
yearly_value = [yearly_payment1, yearly_payment2 + yearly_payment1*growth_rate]
for i in range(2, years_forecast):
    yearly_value.append((yearly_payment1*growth_rate**i + (i-1)*yearly_payment2*growth_rate**(i-1)))

data = {
    'Age' : age_array,
    'Yearly Payments' : yearly_value

}


plot_me = pd.DataFrame(data)
print(plot_me)
print(growth_rate)


plt.figure(figsize=(10,6))
plt.plot(plot_me['Yearly Payments'], label='Savings', color='green', lw=2)
plt.title(f'Savings', fontweight = 'bold')
plt.xlabel('Years')
plt.ylabel('Value (£)')

plt.legend()
plt.tight_layout()
plt.show()