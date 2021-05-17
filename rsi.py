import pandas_datareader as pdr
import datetime
from matplotlib import pyplot as plt

SP500 = 'SPY'


def getTickerData(universe, startDate, endDate):
    data = pdr.get_data_yahoo(universe, startDate, endDate)
    data.index = data.index.date
    return data


def calcRSI(data, period):
    data['delta'] = data['Close'].diff()
    data['up'] = data['delta'].clip(lower=0)
    data['down'] = -1 * data['delta'].clip(upper=0)

    ewmUp = data['up'].ewm(com=period, adjust=False).mean()
    ewmDown = data['down'].ewm(com=period, adjust=False).mean()

    rs = ewmUp / ewmDown
    data['rsi'] = 100 - (100 / (1 + rs))

    return data

def plotRSI(data):
    plt.figure(figsize=(20, 3))
    plt.plot(data.loc[:, 'rsi'])
    plt.show()

if __name__ == '__main__':
    start = datetime.date(2018, 1, 1).strftime(format='%Y-%m-%d')
    end = datetime.date(2021, 5, 14).strftime(format='%Y-%m-%d')
    period = 13
    data = getTickerData('CAT', start, end)
    data = calcRSI(data, period)
    plotRSI(data)
