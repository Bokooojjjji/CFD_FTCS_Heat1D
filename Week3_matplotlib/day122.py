import matplotlib.pyplot as plt
import numpy as np
# 生成数据
x = np.linspace(-3, 3, 50)
y1 = 2*x + 1
y2 = x**2

# 创建图形
plt.figure()

# 设置坐标轴范围
plt.xlim((-1, 2))
plt.ylim((-2, 3))

# 设置坐标轴刻度
new_sticks = np.linspace(-1, 2, 5)
plt.xticks(new_sticks)

# 设置坐标轴标签
plt.yticks([-2, -1.8, -1, 1.22, 3],
           [r'$really\ bad$', r'$bad$', r'$normal$', r'$good$', r'$really\ good$'])

# 绘制曲线
l1, = plt.plot(x, y1, label='linear line')
l2, = plt.plot(x, y2, color='red', linewidth=1.0, linestyle='--', label='square line')

# 添加图例
plt.legend(handles=[l1, l2], labels=['up', 'down'],  loc='best')

# 显示图形
plt.show()