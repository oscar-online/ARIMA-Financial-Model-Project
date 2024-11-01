#
from tabulate import tabulate
import matplotlib.pyplot as plt
import yfinance as yf
import matplotlib.dates as mdates
from datetime import datetime, timedelta


from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tools.sm_exceptions import ValueWarning, HessianInversionWarning, ConvergenceWarning
from statsmodels.tsa.api import VAR

import numpy as np
import seaborn as sns
import pandas as pd
from tqdm import tqdm


import warnings
warnings.simplefilter('ignore', ValueWarning)
warnings.simplefilter('ignore', HessianInversionWarning)
warnings.simplefilter('ignore', ConvergenceWarning)

sns.set_theme()
#
Carbon_Pricing = pd.read_excel('C:\\Users\\oscar.smith\\Desktop\\xlsx\\Energy Markets Data.xlsx')
Emissions_Data = pd.read_csv("C:\\Users\\oscar.smith\\Desktop\\xlsx\\co2_emissions_CREA.csv")
Carbon_Pricing.ECARBIX
Carbon_values = pd.Series(Carbon_Pricing.ECARBIX)
Carbon_values.index = pd.to_datetime(Carbon_Pricing.Date)
Emissions_values = pd.Series(Emissions_Data.value)
Emissions_values.index = pd.to_datetime(Emissions_Data.date, dayfirst=True)
EMV = Emissions_values['2023-10-02':'2024-08-02']
fig, ax1 = plt.subplots(2, 1, figsize=(12,8), sharex = True)
ax1[0].plot(EMV, label='Price', color='blue')
ax1[0].set_title(f'Daily Emissions (Energy Sector)')
ax1[0].set_ylabel('mT')
ax1[0].legend(loc='upper left')
ax1[0].grid()

ax1[1].plot(np.log(Carbon_values), label='Returns', color='orange')
ax1[1].set_title('Daily Close: ECarbix EEX')
ax1[1].set_ylabel('eur/mT')
ax1[1].set_xlabel('Date')
ax1[1].legend(loc='upper left')
ax1[1].grid()

plt.tight_layout()
plt.show()