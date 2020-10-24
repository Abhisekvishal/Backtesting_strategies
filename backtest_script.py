import time
import backtrader as bt
import pandas as pd
from strategy import TestStrategy
import datetime

x = time.time()

cerebro = bt.Cerebro()

cerebro.broker.setcash(1000000)

df = pd.read_csv('oracle',
                 sep=',',
                 # skiprows=1,
                 parse_dates=True,
                 index_col=0)

data = bt.feeds.PandasData(dataname=df,
                           fromdate=datetime.date(2000, 1, 1),
                           todate=datetime.date(2000, 12, 31))


cerebro.adddata(data)

cerebro.addstrategy(TestStrategy)

cerebro.addsizer(bt.sizers.FixedSize, stake=20000)

print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())

cerebro.run()

print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())

cerebro.plot(style='candlestic', barup='limegreen', bardown='red')

print(time.time() - x)
