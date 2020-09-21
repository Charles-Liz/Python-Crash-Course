#!/usr/bin/python
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
x_values = list(range(1,5001))
y_values = [x**3 for x in x_values]
plt.rcParams['font.sans-serif']='SimHei'
plt.scatter(x_values,y_values,s=40,edgecolors='none',c=y_values,cmap=plt.cm.Blues)

#设置图表标题并给坐标轴加上标签
plt.title('Cube Of Numbers',fontsize=24)
plt.xlabel('x轴',fontsize=14)
plt.ylabel('y轴',fontsize=14)
plt.axis([0,6000,0,130000000000])
#自动保存图表 要在show之前保存
plt.savefig('cube_plot1.jpg',bbox_inches='tight')
plt.show()
