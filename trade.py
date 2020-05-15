from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import datetime 
import os

#Import the backtrader platform
import backtrader as bt
from Strategy import TestStrategy


if __name__ == '__main__':
    # Create a cerebro entity
    cerebro = bt.Cerebro()

     

    # Datas are in a subfolder of the samples. Need to find where the script is
    # because it could have been called from anywhere
    modpath = os.path.dirname(os.path.abspath(__file__))
    data = os.path.join(modpath, 'datas/oracle.txt')

    # Create a Data Feed
    data = bt.feeds.YahooFinanceCSVData(
        dataname=data,
        # Do not pass values before this date
        fromdate=datetime.datetime(2000, 1, 1),
        # Do not pass values after this date
        todate=datetime.datetime(2000, 12, 31),
        reverse=False)

    # Add the Data Feed to Cerebro
    cerebro.adddata(data)

    # Add a strategy
    cerebro.addstrategy(TestStrategy) 

    # Set our desired cash start
    cerebro.broker.setcash(100000.0)

    # Print out the starting conditions
    print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())

    # Run over everything
    cerebro.run()

    # Print out the final result
    print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())