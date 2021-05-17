import pandas_datareader as pdr
import datetime

UNIVERSE = 'SPY' # SP500

def getTickerData(universe, startDate, endDate):
    data = pdr.get_data_yahoo(universe, startDate, endDate)
    data.index = data.index.date
    return data
