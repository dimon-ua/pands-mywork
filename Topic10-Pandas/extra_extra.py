import pandas as pd
import re
import matplotlib.pyplot as plt


def clearSqrBrackets(string):
    return 

path = './data/'
logFilename = path + 'access.log.demo'

colNames= ('ip',
    'dash1', 
    'userId', 
    'time', 
    'url', 
    'status code', 
    'size of response', 
    'referer', 
    'user agent', 
    'dunno'
)
df = pd.read_csv(logFilename, sep=' ', header= None, names=colNames)

print(df)

# drop columns
df.drop(columns=['dash1', 'userId'], inplace=True)


df['time'] = df['time'].apply(lambda x: re.search('[\w:/]+', x).group())


df['time'] = pd.to_datetime(df['time'], format='%d/%b/%Y:%H:%M:%S')
print (df.dtypes)

print(df.iloc[0])

start_date = pd.to_datetime('2021/02/15 23:00')
end_date = pd.to_datetime('2021/02/15 23:59:59')


df = df.set_index(['time'])
# newdf = df['2021/02/15 23:00':'2021/02/15 23:59:59']
# print (newdf)


downloadSamples = df['size of response'].resample(rule='30Min').mean()
print(downloadSamples)


downloadSamples.plot()
plt.show()

