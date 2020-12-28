# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 22:15:48 2020

@author: rob
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 14:42:37 2020

@author: rob
"""


import pandas_datareader.data as web

import matplotlib.pyplot as plt

dia = web.DataReader("DIA",
                      start='2020-1-1',
                      end='2020-7-1',
                      data_source='yahoo')

ibm = web.DataReader("IBM",
                      start='2020-1-1',
                      end='2020-7-1',
                      data_source='yahoo')

msft = web.DataReader("MSFT",
                      start='2020-1-1',
                      end='2020-7-1',
                      data_source='yahoo')

googl = web.DataReader("GOOGL",
                      start='2020-1-1',
                      end='2020-7-1',
                      data_source='yahoo')


### making smaller visualizations ###

dia1 = dia[['High', 'Low']]
ibm1 = ibm[['High', 'Low']]
msft1 = msft[['High', 'Low']]
googl1 = googl[['High', 'Low']]


### creating figure 1 ###

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.plot(dia1['High'], 'k', label='DIA')
ax.plot(ibm1['High'], 'r', label='IBM')
ax.plot(msft1['High'], 'g', label='MSFT')
ax.plot(googl1['High'], 'b', label='GOOGL')
ax.legend(loc='best')

fig

### creating figure 2 ###

fig2 = plt.figure()
ax1 = fig2.add_subplot(2,2,1)
ax2 = fig2.add_subplot(2,2,2)
ax3 = fig2.add_subplot(2,2,3)
ax4 = fig2.add_subplot(2,2,4)

_ = ax1.plot(dia1['Low'])
ax2.plot(ibm1['Low'])
ax3.plot(msft1['Low'])
ax4.plot(googl1['Low'])


fig2.text(0.05, 0.5, "Low Stock Price", ha='center', va='center', rotation=90)
fig2.text(0.5, 0.05, "Date", ha='center', va='center')

fig2