import pandas as pd
import pandas_datareader as pdr
import numpy as np
from utils import *

pd.set_option('display.max_rows', 100)
pd.set_option('display.max_columns', 100)

def mfi(df, n):
    df['typical_price'] = (df.High + df.Low + df.Close) / 3
    df['sign'] = np.sign(df.typical_price - df.typical_price.shift(1))
    df['raw_flow'] = df.typical_price * df.Volume * df.sign
    df['pos_flow'] = df.raw_flow * (df.sign > 0)
    df['neg_flow'] = df.raw_flow * (df.sign < 0)
    df['flow_ratio'] = np.abs(df.pos_flow.rolling(14).sum() / df.neg_flow.rolling(14).sum())
    df['mfi'] = 100 - (100 / (1 + df.flow_ratio))


    return df


if __name__ == '__main__':
    df = getTickerData('AMT', datetime.date(2019, 5, 1), datetime.date(2021, 5, 21))
    res = mfi(df, 14)
    print(res)
    plotRSI(res, 'mfi')
