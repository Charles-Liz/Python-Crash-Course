# @Author  : lizhao
# @Time    : 2020/9/23 22:13
# @Function:
import pygal
from die import Die
#创建一个D6
die1 = Die(8)
die2 = Die(8)
#掷几次骰子，并将其结果存储到一个列表中
results=[]
for roll_num in range(1000):
    result = die1.roll()*die2.roll()
    results.append(result)
#分析结果
frequencies = []
max_results = die1.num_sides*die2.num_sides
for value in range(1,max_results+1):
    frequency = results.count(value)
    frequencies.append(frequency)
#对结果进行可视化
hist = pygal.Bar()
hist.title = 'Results of rolling two D6 1000 times.'
hist.x_labels = [value for value in range(1,max_results+1)]
hist.x_title = 'Results'
hist.y_title = 'Frequency of Result'

hist.add('D8*D8',frequencies)
hist.render_to_file('die_visual.svg')
