from datetime import date
from nsepy import get_history,get_index_pe_history
#pip install nsepy   to install nsepy library
'''sbin=get_history(symbol="SBIN",start=date(2021,1,1), end=date(2021,1,29))
print(sbin)'''

import pandas as pd
'''try:
    nifty = pd.read_csv('C:\\Mydrive\\Study\\workspace\\data\\nifty2020year_withPE.csv')
    print('Read from disk successful')
except:'''
datadirectory="C:\\data\\"
startyear=2019
endyear=2020
'''scriptName='NIFTY'
istheScriptIndex=True'''
scriptName='SBIN'
istheScriptIndex=False  #change this to True if fetch is for Index data
for x in range(startyear,endyear):	
    print('Downloading from NSE' + str(x))
    if(istheScriptIndex):
    	sciptData = get_history(scriptName, date(x, 1, 1), date(x, 12, 31), index=True)
    else:
    	sciptData = get_history(scriptName, date(x, 1, 1), date(x, 12, 31))
    pe = get_index_pe_history(scriptName, date(x, 1, 1), date(x, 12, 31))
    sciptData['PE'] = pe['P/E']
    sciptData.to_csv(datadirectory + scriptName + str(x) + 'year_withPE.csv')
    print('completed for year ' + str(x))

print('completed')


