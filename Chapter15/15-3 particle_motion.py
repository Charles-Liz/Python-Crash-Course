# @Author  : lizhao
# @Time    : 2020/9/23 14:10
# @Function:
import matplotlib.pyplot as plt
from random_walk import RandomWalk

rw = RandomWalk()
rw.fill_walk()

point_numbers = list(range(rw.num_points))
plt.plot(rw.x_values,rw.y_values)
plt.axes().get_xaxis().set_visible(False)
plt.axes().get_yaxis().set_visible(False)

plt.show()
