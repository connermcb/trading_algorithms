import pandas_datareader
import pandas as pd
import numpy as np
from utils import *

def pfe(df, n):
    num = np.sqrt((df.Close - df.Close.shift(n))**2 + n**2)
    denom = np.sqrt((df.Close[:-2] - df.Close.shift(1)[:-2])**2 + 1).sum()
    print(denom)
    df['pfe'] = 100 * (num / denom)
    df['sign'] = np.sign(df.Close - df.Close.shift(n))
    df['pfe'] = df.pfe * df.sign
    df['pfe'] = df.pfe.ewm(span=n, adjust=False).mean()
    return df

if __name__ == '__main__':
    df = getTickerData('AMT', datetime.date(2019, 5, 1), datetime.date(2019, 8, 31))
    print(df[-14:])
    # print(df.Close.shift(14))
    # plotRSI(pfe(df, 14), 'pfe')
