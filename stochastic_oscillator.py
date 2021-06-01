import pandas as pd
import pandas_datareader as pdr
import numpy as np
from utils import *

def stochastic_oscillator(df, n):
    df['period_min'] = df.Low.rolling(window=n).min()
    df['period_max'] = df.High.rolling(window=n).max()

    ratio = (df.Close - df.period_min) / (df.period_max - df.period_min)
    df['fast_stoch_osc'] = 100 * ratio
    df['slow_stoch_osc'] = df.fast_stoch_osc.rolling(3).mean()

    return df


if __name__ == '__main__':
    df = getTickerData('AMT', datetime.date(2019, 5, 1), datetime.date(2019, 8, 31))
    res = stochastic_oscillator(df, 14)
    print(res.Volume)
    plotRSI(res, ['fast_stoch_osc','slow_stoch_osc'])