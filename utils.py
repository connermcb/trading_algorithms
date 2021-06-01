import pandas as pd
import pandas_datareader as pdr
import datetime
from matplotlib import pyplot as plt

def getTickerData(universe, startDate, endDate):
    data = pdr.get_data_yahoo(universe, startDate, endDate)
    data.index = data.index.date
    return data


def plotRSI(data, indicator):
    plt.figure(figsize=(20, 3))
    plt.plot(data.loc[:, indicator])
    plt.show()
