from utils import *
import pandas as pd


def calcMACD(data):

    data['12'] = data.ewm('Close', 12)
    data['26'] = data.ewm('Close', 26)
    data['delta'] = data['12'] - data['26']
    data['macd'] = data.ewm('delta', 9)

    return data

if __name__ == '__main__':
    ticker = 'CAT'
    start = datetime.date(2018, 1, 1).strftime(format='%Y-%m-%d')
    end = datetime.date(2021, 5, 14).strftime(format='%Y-%m-%d')
    period = 13
    data = getTickerData(ticker, start, end)
    data = calcMACD(data, period)
    plotRSI(data, 'macd')
