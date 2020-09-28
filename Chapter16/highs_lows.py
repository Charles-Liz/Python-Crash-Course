#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Author  : lizhao
# @Time    : 2020/9/27 20:49
# @Function:
import csv
from matplotlib import pyplot as plt
from datetime import datetime
filename1 = 'sitka_weather_2014.csv'
filename2 = 'death_valley_2014.csv'
def get_weather_data(filename,dates,highs,lows):
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        for row in reader:
            try:
                current_date = datetime.strptime(row[0],"%Y-%m-%d")
                high = int(row[1])
                low = int(row[3])
            except ValueError:
                print(datetime,'missing data')
            else:
                dates.append(current_date)
                highs.append(high)
                lows.append(lows)

#get sitka weather
dates,highs,lows=[],[],[]
get_weather_data(filename1,dates,highs,lows)

#plot sitka
fig = plt.figure(dpi=128,figsize=(10,6))
plt.plot(dates,highs,c='red',alpha=0.6)
plt.plot(dates,lows,c='blue',alpha=0.6)

#get death weather
dates,highs,lows=[],[],[]
get_weather_data(filename2,dates,highs,lows)

#plot death
plt.plot(dates,highs,c='red')
plt.plot(dates,lows,c='blue')

plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False

plt.xlabel('',fontsize = 16)
fig.autofmt_xdate()#绘制斜的日期标签
plt.ylabel('温度',fontsize = 16)
plt.title('Daily high temperatures,July 2014')
plt.show()