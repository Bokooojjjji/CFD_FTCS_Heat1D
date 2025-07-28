#Contours图
# 导入 matplotlib 库中的 pyplot 模块，它是 Python 里常用的绘图工具，后续用它来绘制等高线图
import matplotlib.pyplot as plt
# 导入 numpy 库，用于高效的数值计算和数组操作，能方便地生成数据点和进行数学运算
import numpy as np

# 定义一个二元函数 f(x, y)，它代表了一个曲面的高度函数
# 函数的具体表达式为 (1 - x / 2 + x**5 + y**3) * np.exp(-x**2 -y**2)
# 后续会用这个函数计算不同 (x, y) 坐标对应的高度值
def f(x,y):
    # the height function
    return (1 - x / 2 + x**5 + y**3) * np.exp(-x**2 -y**2)

# 设置网格点的数量为 256 个
# 这个数量决定了后续生成的网格的精细程度，数量越多，图形越精细
n = 256

# 使用 np.linspace 函数生成一个包含 n 个元素的数组
# 这些元素均匀分布在 -3 到 3 这个区间内，作为 x 轴上的坐标点
x = np.linspace(-3, 3, n)
# 同理，生成一个包含 n 个元素的数组，均匀分布在 -3 到 3 区间内，作为 y 轴上的坐标点
y = np.linspace(-3, 3, n)

# 使用 np.meshgrid 函数将 x 和 y 数组转换为二维网格坐标矩阵
# X 是一个二维数组，它的每一行都是 x 数组的复制
# Y 是一个二维数组，它的每一列都是 y 数组的复制
# 这样 X 和 Y 就构成了一个完整的二维网格，方便后续计算每个网格点的函数值
X,Y = np.meshgrid(x, y)

# 使用 plt.contourf 函数绘制填充等高线图
# X 和 Y 是网格坐标矩阵，f(X, Y) 是每个网格点对应的函数值
# 8 表示将等高线分为 8 个等级，也就是会有 8 个不同颜色的区域
# alpha=.75 表示设置填充区域的透明度为 0.75，让图形看起来更柔和
# cmap=plt.cm.hot 表示使用 'hot' 颜色映射，让不同高度的区域用不同的热色表示
plt.contourf(X, Y, f(X, Y), 8, alpha=.75, cmap=plt.cm.hot)

# 使用 plt.contour 函数绘制等高线线条
# 同样传入 X、Y 和 f(X, Y)，8 表示等高线等级数
# colors='black' 表示等高线线条颜色为黑色
# linewidth=.5 表示等高线线条的宽度为 0.5
C = plt.contour(X, Y, f(X, Y), 8, colors='black', linewidth=.5)

# 使用 plt.clabel 函数为等高线添加标签
# C 是之前绘制的等高线对象
# inline=True 表示将标签放在等高线内部
# fontsize=10 表示标签的字体大小为 10
plt.clabel(C, inline=True, fontsize=10)

# 不显示 x 轴的刻度标签，让图形更简洁
plt.xticks(())
# 不显示 y 轴的刻度标签，让图形更简洁
plt.yticks(())

# 如果你想显示图形，需要添加这行代码
plt.show()