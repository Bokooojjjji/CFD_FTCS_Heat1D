#Scatter散点图
# 导入 matplotlib 库的 pyplot 模块，它是 Python 里强大的绘图工具，之后用它来绘制散点图
import matplotlib.pyplot as plt
# 导入 numpy 库，这个库用于高效的数值计算，能方便地生成随机数据
import numpy as np

# 设定数据点的数量为 1024 个，后续就会生成 1024 个数据点用于绘图
n = 1024    # data size

# 利用 numpy 的 random.normal 函数生成 n 个服从正态分布（高斯分布）的随机数
# 第一个参数 0 是正态分布的均值，意味着数据大致围绕 0 分布
# 第二个参数 1 是正态分布的标准差，反映了数据的离散程度
# 这些随机数作为每个数据点的 X 坐标值
X = np.random.normal(0, 1, n) # 每一个点的X值

# 同理，再次使用 random.normal 函数生成 n 个服从正态分布的随机数
# 同样均值为 0，标准差为 1，这些随机数作为每个数据点的 Y 坐标值
Y = np.random.normal(0, 1, n) # 每一个点的Y值

# 用 numpy 的 arctan2 函数计算每个数据点相对于原点的角度（以弧度为单位）
# 这个角度值将作为每个数据点的颜色依据，不同角度对应不同颜色
T = np.arctan2(Y, X) # for color value

# 使用 pyplot 的 scatter 函数绘制散点图
# 传入 X 和 Y 作为散点的坐标
# s=75 表示设置每个散点的大小为 75
# c=T 表示根据 T（角度值）为每个散点指定颜色，会形成颜色渐变效果
# alpha=.5 表示设置散点的透明度为 0.5，让图形看起来更柔和
plt.scatter(X, Y, s=75, c=T, alpha=.5)

# 设置 x 轴的显示范围，让图形在 x 轴上只显示 -1.5 到 1.5 之间的部分
plt.xlim(-1.5, 1.5)
# 传入空元组，这样就不会显示 x 轴上的刻度，让图形更简洁
plt.xticks(())  # ignore xticks

# 设置 y 轴的显示范围，让图形在 y 轴上只显示 -1.5 到 1.5 之间的部分
plt.ylim(-1.5, 1.5)
# 传入空元组，不显示 y 轴上的刻度，保持图形简洁
plt.yticks(())  # ignore yticks

# 调用 show 函数将绘制好的散点图显示出来
plt.show()