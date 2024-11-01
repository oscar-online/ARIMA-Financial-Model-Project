from flask import Flask, render_template, request
import io
import base64
import matplotlib.pyplot as plt
import yfinance as yf
import matplotlib.dates as mdates
import os
from datetime import datetime, timedelta


from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tools.sm_exceptions import ValueWarning, HessianInversionWarning, ConvergenceWarning
from arch import arch_model

import numpy as np
import seaborn as sns
import pandas as pd
from tqdm import tqdm


import warnings
warnings.simplefilter('ignore', ValueWarning)
warnings.simplefilter('ignore', HessianInversionWarning)
warnings.simplefilter('ignore', ConvergenceWarning)
#We begin by importing the necessary libraries



app = Flask(__name__)

def yf_plot(Ticker, start, end):
    Price_1 = yf.download(Ticker, start, end).Close
    Returns_1 = Price_1.pct_change().dropna()
    fig, ax1 = plt.subplots(2, 1, figsize=(10, 6), sharex=True)
    ax1[0].plot(Price_1.index, Price_1, label='Price', color='red')
    ax1[0].set_title(f'Daily Close: Price ${Ticker}')
    ax1[0].set_ylabel('Price ($)')
    ax1[0].legend(loc='upper left')
    ax1[0].grid()

    ax1[1].plot(Returns_1.index, Returns_1, label='Returns', color='blue')
    ax1[1].set_title('First Order Difference (Returns)')
    ax1[1].set_ylabel(f'Returns ${Ticker}')
    ax1[1].set_xlabel('Date')
    ax1[1].axhline(y=0, color='black', linestyle="--")
    ax1[1].legend(loc='upper left')
    ax1[1].grid()

    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    plt.close(fig)
    return base64.b64encode(buf.getvalue()).decode('utf8')

@app.route('/', methods=['GET', 'POST'])
def index():
    plot_url = None
    if request.method == 'POST':
        ticker = request.form['ticker']
        start = request.form['start']
        end = request.form['end']
        plot_url = yf_plot(ticker, start, end)

    return render_template('ARIMAsite.html', plot_url=plot_url)

if __name__ == '__main__':
    app.run(debug=False)











