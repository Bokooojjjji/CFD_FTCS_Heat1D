# 导入 matplotlib 库的 pyplot 模块，用于绘图，通常将其重命名为 plt 方便后续使用
import matplotlib.pyplot as plt
# 导入 numpy 库，用于进行数值计算，通常将其重命名为 np 方便后续使用
import numpy as np

# 使用 np.linspace 函数生成一个包含 50 个元素的数组
# 这 50 个元素均匀分布在 -3 到 3 这个区间内，作为 x 轴的数据点
x = np.linspace(-3, 3, 50)
# 根据公式 y = 0.1 * x 计算每个 x 对应的 y 值
# 这里使用了 numpy 数组的广播特性，能高效地对整个 x 数组进行计算
y = 0.1 * x

# 创建一个新的绘图窗口，用于后续绘制图形
plt.figure()

# 绘制 x 和 y 对应的曲线
# linewidth=10 表示设置曲线的线宽为 10，让曲线更粗更明显
# zorder=1 用于设置该曲线在 z 轴方向的层级顺序，值越小越靠后
plt.plot(x, y, linewidth=10, zorder=1)

# 设置 y 轴的显示范围，让图形只显示 y 值在 -2 到 2 之间的部分
plt.ylim(-2, 2)

# 获取当前的坐标轴对象，后续可以对该坐标轴进行各种设置
ax = plt.gca()

# 将坐标轴的右边框颜色设置为透明，即不显示右边框
ax.spines['right'].set_color('none')
# 将坐标轴的上边框颜色设置为透明，即不显示上边框
ax.spines['top'].set_color('none')

# 设置 x 轴的刻度标签显示在底部
ax.xaxis.set_ticks_position('bottom')
# 将 x 轴的位置设置为数据值为 0 的位置，也就是让 x 轴穿过原点
ax.spines['bottom'].set_position(('data', 0))

# 设置 y 轴的刻度标签显示在左边
ax.yaxis.set_ticks_position('left')
# 将 y 轴的位置设置为数据值为 0 的位置，也就是让 y 轴穿过原点
ax.spines['left'].set_position(('data', 0))

# 获取 x 轴和 y 轴的所有刻度标签，将它们组合成一个列表
for label in ax.get_xticklabels() + ax.get_yticklabels():
    # 设置刻度标签的字体大小为 12
    label.set_fontsize(12)
    # 为刻度标签添加一个背景框
    # facecolor='white' 表示背景框的填充颜色为白色
    # edgecolor='None' 表示背景框没有边框
    # alpha=0.7 表示背景框的透明度为 0.7
    # zorder=2 表示该背景框在 z 轴方向的层级顺序，值越大越靠前
    label.set_bbox(dict(facecolor='white', edgecolor='None', alpha=0.7, zorder=2))

# 显示绘制好的图形
plt.show()