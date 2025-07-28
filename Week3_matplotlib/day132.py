#Bar柱状图
# 导入 matplotlib 库中的 pyplot 模块，用于绘图
import matplotlib.pyplot as plt
# 导入 numpy 库，用于进行数值计算和数组操作
import numpy as np

# 定义柱子的数量，这里设置为 12 个
n = 12
# 使用 np.arange(n) 生成一个从 0 到 n-1 的整数数组，作为 x 轴上柱子的位置
X = np.arange(n)
# 计算第一组柱子的高度 Y1
# 1 - X / float(n) 是一个随着 X 增大而减小的系数
# np.random.uniform(0.5, 1.0, n) 生成 n 个在 0.5 到 1.0 之间的随机数
# 两者相乘得到每个柱子的高度，这些高度是随机且递减的
Y1 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)
# 计算第二组柱子的高度 Y2，原理同 Y1
Y2 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)

# 绘制第一组正向的柱子，默认颜色和样式
plt.bar(X, +Y1)
# 绘制第二组负向的柱子，默认颜色和样式
plt.bar(X, -Y2)

# 设置 x 轴的显示范围，从 -0.5 到 n，确保所有柱子都能完整显示
plt.xlim(-.5, n)
# 不显示 x 轴的刻度标签，使图形更简洁
plt.xticks(())
# 设置 y 轴的显示范围，从 -1.25 到 1.25，保证正负柱子都能完整显示
plt.ylim(-1.25, 1.25)
# 不显示 y 轴的刻度标签，使图形更简洁
plt.yticks(())

# 重新绘制第一组正向的柱子，并设置柱子的填充颜色为 '#9999ff'（浅紫色），边框颜色为白色
plt.bar(X, +Y1, facecolor='#9999ff', edgecolor='white')
# 重新绘制第二组负向的柱子，并设置柱子的填充颜色为 '#ff9999'（浅红色），边框颜色为白色
plt.bar(X, -Y2, facecolor='#ff9999', edgecolor='white')

# 遍历 X 和 Y1 数组，为正向柱子添加数据标签
for x, y in zip(X, Y1):
    # 在每个柱子上方添加数据标签
    # x + 0.4 是标签的 x 坐标位置，让标签位于柱子上方中间
    # y + 0.05 是标签的 y 坐标位置，让标签稍微高于柱子顶部
    # '%.2f' % y 是将 y 值格式化为保留两位小数的字符串
    # ha='center' 表示水平居中对齐
    # va='bottom' 表示垂直底部对齐
    plt.text(x + 0.4, y + 0.05, '%.2f' % y, ha='center', va='bottom')

# 遍历 X 和 Y2 数组，为负向柱子添加数据标签
for x, y in zip(X, Y2):
    # 在每个负向柱子下方添加数据标签
    # x + 0.4 是标签的 x 坐标位置，让标签位于柱子下方中间
    # -y - 0.05 是标签的 y 坐标位置，让标签稍微低于柱子底部
    # '%.2f' % y 是将 y 值格式化为保留两位小数的字符串
    # ha='center' 表示水平居中对齐
    # va='top' 表示垂直顶部对齐
    plt.text(x + 0.4, -y - 0.05, '%.2f' % y, ha='center', va='top')

# 显示绘制好的图形
plt.show()