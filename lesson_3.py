# Задача 1
import pandas as pd

download_url = ('12345.csv')

table = pd.read_csv(download_url,sep=";")
type(table)
pd.core.frame.DataFrame
pd.set_option('display.max.columns', None)
print(table.head())

# Задача 2
import pandas as pd
import matplotlib.pyplot as plt
download_url = ('12345.csv')

table = pd.read_csv(download_url,sep=";")
type(table)
a = table['Количество кликов'].tolist()
print('Количество кликов:',a)
b = table['Количетсво показов'].tolist()
print('Количество показов:',b)
pd.core.frame.DataFrame
pd.set_option('display.max.columns', None)

plt.plot(b,a)
plt.show()