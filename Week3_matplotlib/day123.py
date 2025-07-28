#Annotation的标注
import matplotlib.pyplot as plt
import numpy as np

# 生成数据
# 使用 np.linspace 生成从 -3 到 3 之间均匀分布的 50 个点作为 x 坐标
x = np.linspace(-3, 3, 50)
# 根据直线方程 y = 2x + 1 计算对应的 y 坐标
y = 2*x + 1

# 创建图形
# 创建一个编号为 1，大小为 8x5 英寸的图形窗口
plt.figure(num=1, figsize=(8, 5))
# 绘制直线，x 为 x 坐标，y 为 y 坐标
plt.plot(x, y)

# 获取当前的坐标轴对象
ax = plt.gca()

# 设置坐标轴样式
# 隐藏右侧的坐标轴
ax.spines['right'].set_color('none')
# 隐藏顶部的坐标轴
ax.spines['top'].set_color('none')
# 将 x 轴的刻度设置在底部
ax.xaxis.set_ticks_position('bottom')
# 将 x 轴设置在 y = 0 的位置
ax.spines['bottom'].set_position(('data', 0))
# 将 y 轴的刻度设置在左侧
ax.yaxis.set_ticks_position('left')
# 将 y 轴设置在 x = 0 的位置
ax.spines['left'].set_position(('data', 0))

# 定义特定点
# 选取 x0 = 1
x0 = 1
# 计算 x0 对应的 y0 值
y0 = 2*x0 + 1

# 绘制垂直线
# 绘制从 (x0, 0) 到 (x0, y0) 的黑色虚线，线宽为 2.5
plt.plot([x0, x0], [0, y0], 'k--', linewidth=2.5)

# 标记特定点
# 在 (x0, y0) 处绘制一个蓝色的散点，散点大小为 50
plt.scatter([x0], [y0], s=50, color='b')

# 添加注释
# 在点 (x0, y0) 处添加注释
# xy=(x0, y0) 表示注释指向的点
# xycoords='data' 表示使用数据坐标
# xytext=(+30, -30) 表示注释文本相对于指向点的偏移量
# textcoords='offset points' 表示偏移量的单位是点
# fontsize=16 表示注释文本的字体大小
# arrowprops 设置箭头的样式，这里使用 -> 样式，连接样式为弧形
plt.annotate(r'$2x+1=%s$' % y0, xy=(x0, y0), xycoords='data', xytext=(+30, -30),
             textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle='->', connectionstyle="arc3,rad=.2"))

# 添加文本
# 在坐标 (-3.7, 3) 处添加红色文本
# fontdict 用于设置文本的字体属性，这里设置字体大小为 16，颜色为红色
plt.text(-3.7, 3, r'$This\ is\ the\ some\ text. \mu\ \sigma_i\ \alpha_t$',
         fontdict={'size': 16, 'color': 'r'})

# 显示图形
plt.show()