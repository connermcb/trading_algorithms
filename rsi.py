import pandas_datareader as pdr
import datetime
from utils import *


def calcRSI(data, period):
    data['delta'] = data['Close'].diff()
    data['up'] = data['delta'].clip(lower=0)
    data['down'] = -1 * data['delta'].clip(upper=0)

    ewmUp = data['up'].ewm(com=period, adjust=False).mean()
    ewmDown = data['down'].ewm(com=period, adjust=False).mean()

    rs = ewmUp / ewmDown
    data['rsi'] = 100 - (100 / (1 + rs))

    return data

if __name__ == '__main__':
    ticker = 'CAT'
    start = datetime.date(2018, 1, 1).strftime(format='%Y-%m-%d')
    end = datetime.date(2021, 5, 14).strftime(format='%Y-%m-%d')
    period = 13
    data = getTickerData(ticker, start, end)
    data = calcRSI(data, period)
    plotRSI(data, 'rsi')
